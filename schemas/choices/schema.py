class SchemaStatusChoices:
    """
    Выборы статуса схемы
    """

    READY = "ready"
    PROCESSING = "processing"
    FAILED = "failed"

    CHOICES = (
        (READY, "Готов к скачиванию"),
        (PROCESSING, "В работе"),
        (FAILED, "Ошибка"),
    )
