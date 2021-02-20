from io import StringIO, BytesIO
from django.core.files import File
from celery import Task
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile

from config.celery import app
from schemas.choices.schema import SchemaStatusChoices
from schemas.models import Schema
import csv

from schemas.services.generate_data import DummyData


class GenerateSchema(Task):
    """
    Создание файла со схемой
    """

    def run(self, schema_id: int, rows: int):
        instance: Schema = Schema.objects.filter(id=schema_id).first()
        try:
            columns = [
                column for column in instance.column_in_schemas.all().order_by("order")
            ]
            f = StringIO()
            f.seek(0)
            writer = csv.writer(f)
            writer.writerow([column.name for column in columns])
            for x in range(rows):
                writer.writerow(
                    [DummyData().column_recognition(column.id) for column in columns]
                )
            csv_file = InMemoryUploadedFile(
                f, None, "schema-{}.csv".format(instance.id), "text/csv", None, "utf-8"
            )
            instance.file = csv_file
            instance.status = SchemaStatusChoices.READY
        except Exception as exc:
            instance.status = SchemaStatusChoices.FAILED
        finally:
            instance.save()


GenerateSchemaTask = app.register_task(GenerateSchema())
