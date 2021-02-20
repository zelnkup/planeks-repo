from django.core.validators import MinValueValidator
from django.db import models

from schemas.choices.column import ColumnTypeChoices
from schemas.models.schema import Schema


class ColumnInSchema(models.Model):
    name = models.CharField("Название", max_length=255)
    type = models.CharField(
        "Тип данных", max_length=30, choices=ColumnTypeChoices.CHOICES
    )
    order = models.PositiveSmallIntegerField(
        "Порядок столбцов", default=1, validators=[MinValueValidator(1)]
    )
    quantity_range_lower = models.PositiveSmallIntegerField(
        "Нижняя граница диапазона чисел", null=True, blank=True
    )
    quantity_range_upper = models.PositiveSmallIntegerField(
        "Верхняя граница диапазона чисел", null=True, blank=True
    )
    schema = models.ForeignKey(
        Schema,
        verbose_name="Схема",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="column_in_schemas",
    )

    class Meta:
        verbose_name = "Столбец в схеме"
        verbose_name_plural = "Столбцы в схеме"

    def __str__(self):
        return "Столбец {} в схеме".format(self.name)
