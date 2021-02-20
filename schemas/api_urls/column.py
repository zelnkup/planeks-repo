from django.urls import path

from schemas.api_views.column import ColumnInSchemeCreateView

urlpatterns = [path("create/", ColumnInSchemeCreateView.as_view())]
