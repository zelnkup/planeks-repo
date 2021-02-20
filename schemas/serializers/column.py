from rest_framework import serializers

from schemas.models import ColumnInSchema


class ColumnInSchemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColumnInSchema
        fields = "__all__"
