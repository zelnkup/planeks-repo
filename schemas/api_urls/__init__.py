from django.urls import path, include

urlpatterns = [
    path("schema/", include("schemas.api_urls.schema")),
    path("column/", include("schemas.api_urls.column")),
]
