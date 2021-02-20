from rest_framework import serializers

from schemas.choices.schema import SchemaStatusChoices
from schemas.models import Schema, ColumnInSchema


class SchemaSerializer(serializers.ModelSerializer):
    columns_to_add = serializers.ListField(
        child=serializers.IntegerField(min_value=0), required=True, write_only=True
    )

    class Meta:
        model = Schema
        exclude = ["user", "file", "status"]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        validated_data["status"] = SchemaStatusChoices.PROCESSING
        columns_to_add = validated_data.pop("columns_to_add")
        instance = super().create(validated_data)
        for column in ColumnInSchema.objects.filter(id__in=columns_to_add):
            column.schema = instance
            column.save()
        return instance


class UserSchemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schema
        fields = ["name", "id", "created_at", "status", "file"]


class RowsSerializer(serializers.Serializer):
    """
    Получение количества столбцов для генерации csv
    """

    rows = serializers.IntegerField(required=True)
