from rest_framework import generics

from schemas.models import ColumnInSchema
from schemas.serializers.column import ColumnInSchemaSerializer


class ColumnInSchemeCreateView(generics.CreateAPIView):
    """
    Создание столбца
    """

    serializer_class = ColumnInSchemaSerializer
    queryset = ColumnInSchema.objects.all()
