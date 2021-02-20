from django.urls import include, path

urlpatterns = [path("schemas/", include("schemas.api_urls"))]
