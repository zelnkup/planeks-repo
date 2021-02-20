from django.contrib import admin

from schemas.admin.column import ColumnInLine
from schemas.models import Schema


@admin.register(Schema)
class SchemaAdmin(admin.ModelAdmin):
    inlines = [ColumnInLine]
    list_display = ["__str__", "status", "created_at"]
