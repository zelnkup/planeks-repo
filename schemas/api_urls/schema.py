from django.urls import path

from schemas.api_views.schema import (
    CreateSchemaView,
    UserSchemaListView,
    GenerateSchemaFileView,
)

urlpatterns = [
    path("create/", CreateSchemaView.as_view()),
    path("list/", UserSchemaListView.as_view()),
    path("generate/", GenerateSchemaFileView.as_view()),
]
