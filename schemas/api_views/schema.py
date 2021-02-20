from rest_framework import generics, permissions, status
from rest_framework.response import Response

from schemas.choices.schema import SchemaStatusChoices
from schemas.models import Schema
from schemas.serializers.schema import (
    SchemaSerializer,
    UserSchemaSerializer,
    RowsSerializer,
)
from schemas.tasks import GenerateSchemaTask


class CreateSchemaView(generics.CreateAPIView):
    """
    Создание схемы
    """

    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserSchemaListView(generics.ListAPIView):
    """
    Получение всех схем пользователя
    """

    serializer_class = UserSchemaSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Schema.objects.all()

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(user=self.request.user)
            .prefetch_related("column_in_schemas")
        )


class GenerateSchemaFileView(generics.GenericAPIView):
    serializer_class = RowsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        rows = serializer.data.get("rows")
        schemas = request.user.schemas.all()
        for schema in schemas:
            schema.status = SchemaStatusChoices.PROCESSING
            schema.save()
            GenerateSchemaTask.delay(schema.id, rows)
        return Response("ok", status=status.HTTP_200_OK)
