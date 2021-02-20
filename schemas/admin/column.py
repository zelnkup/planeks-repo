from django.contrib import admin

from schemas.models import ColumnInSchema


class ColumnInLine(admin.StackedInline):
    model = ColumnInSchema


@admin.register(ColumnInSchema)
class ColumnInSchemaAdmin(admin.ModelAdmin):
    list_display = ["__str__", "type", "schema"]
