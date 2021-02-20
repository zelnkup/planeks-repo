class ColumnTypeChoices:
    """
    Выборы типов столбца
    """

    INT = "integer"
    DATE = "date"
    EMAIL = "email"
    PHONE = "phone"
    JOB = "job"

    CHOICES = (
        (INT, "Number range"),
        (DATE, "Date time"),
        (EMAIL, "E-mail"),
        (PHONE, "Phone number"),
        (JOB, "Job position"),
    )
