from django.db import models

from schemas.choices.schema import SchemaStatusChoices
from users.models import User


class Schema(models.Model):
    name = models.CharField("Название", max_length=255)
    created_at = models.DateTimeField("Создан в ", auto_now_add=True)
    status = models.CharField(
        "Статус", choices=SchemaStatusChoices.CHOICES, max_length=255
    )
    file = models.FileField("Схема", blank=True, null=True, upload_to="schemas/")
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        related_name="schemas",
    )

    class Meta:
        verbose_name = "Схема"
        verbose_name_plural = "Схемы"

    def __str__(self):
        return "Схема {} создана {}".format(self.name, self.created_at)
