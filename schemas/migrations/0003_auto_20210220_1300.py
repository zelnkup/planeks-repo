# Generated by Django 3.1.7 on 2021-02-20 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("schemas", "0002_schema_user")]

    operations = [
        migrations.AlterField(
            model_name="columninschema",
            name="schema",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="schemas.schema",
                verbose_name="Схема",
            ),
        )
    ]
