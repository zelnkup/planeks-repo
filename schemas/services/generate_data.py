import json
import string
from datetime import datetime
from typing import Union

from schemas.choices.column import ColumnTypeChoices
from schemas.models import ColumnInSchema
import random
from random import randrange
from datetime import timedelta


class DummyData:
    """
    Определение типа столбца и генерация данных
    """

    @staticmethod
    def __random_date(start: datetime, end: datetime) -> datetime:
        """
        Рандомная дата между двумя периодами
        :param start:
        :param end:
        :return:
        """
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        return start + timedelta(seconds=random_second)

    @staticmethod
    def _generate_int_data(column: ColumnInSchema) -> int:
        """
        Рандомное значение между двумя числами
        :param column:
        :return:
        """
        return random.randint(column.quantity_range_lower, column.quantity_range_upper)

    def _generate_date_data(self) -> datetime:
        """
        Рандомная дата между двумя периодами времени
        :return:
        """
        return self.__random_date(
            datetime.strptime("1/1/2020 4:50 AM", "%m/%d/%Y %I:%M %p"),
            datetime.strptime("1/1/2021 4:50 AM", "%m/%d/%Y %I:%M %p"),
        )

    @staticmethod
    def _generate_job_data() -> str:
        """
        Рандомное название професии с json фикстуры
        :return:
        """
        with open("schemas/utils/jobs.json") as f:
            data = json.load(f)
        job_titles = data.get("jobs")
        return random.choices(job_titles)[0]

    @staticmethod
    def __get_random_name() -> str:
        """
        Случайные буквы с алфавита
        :return:
        """
        return "".join(
            random.choice(string.ascii_letters) for x in range(random.randint(5, 15))
        )

    def _generate_email_data(self):
        """
        Создание рандомных емейлов
        :return:
        """
        domains = ["hotmail.com", "gmail.com", "proton.mail", "mail.ru", "yahoo.com"]
        return self.__get_random_name() + "@" + random.choice(domains)

    @staticmethod
    def __get_country_code() -> str:
        """Выбор рандомного кода страны"""
        with open("schemas/utils/codes.json") as f:
            data = json.load(f)
        country_code = data.get("codes")
        return random.choices(country_code)[0]["dial_code"]

    def _generate_phone_data(self) -> str:
        """
        Выбор рандомного кода страны
        :return:
        """
        return self.__get_country_code() + "".join(
            str(random.randint(0, 9)) for x in range(random.randint(5, 9))
        )

    def column_recognition(self, column_id: int) -> Union[int, str, datetime]:
        """
        Проверка стобцов по статусу и генерация fake data
        :param column_id:
        :param rows:
        :return:
        """
        column = ColumnInSchema.objects.filter(id=column_id).first()
        if column.type == ColumnTypeChoices.INT:
            return self._generate_int_data(column)
        elif column.type == ColumnTypeChoices.DATE:
            return self._generate_date_data()
        elif column.type == ColumnTypeChoices.JOB:
            return self._generate_job_data()
        elif column.type == ColumnTypeChoices.EMAIL:
            return self._generate_email_data()
        elif column.type == ColumnTypeChoices.PHONE:
            return self._generate_phone_data()
        else:
            return "not known data"
