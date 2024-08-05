import re

from src.utils.currency_handler import get_currency_transfer


class Vacancy:
    def __init__(self, name, city, salary_from, salary_to, currency, requirements, link):
        self.name = name
        self.city = city

        if salary_from:
            self.salary_from = salary_from
        else:
            self.salary_from = 0

        if salary_to:
            self.salary_to = salary_to
        else:
            self.salary_to = 0

        self.currency = currency
        self.requirements = requirements
        self.link = link

    def __repr__(self):
        """
        Магический метод для отображения объекта
        в понятном для пользователя виде

        :return: (str) строковое отображение объекта
        """
        if self.salary_from == 0 and self.salary_to == 0 and self.currency is None:
            return (f"\n{"-" * 50}\n\n"
                    f"Название вакансии: {self.name}\n"
                    f"Город: {self.city}\n"
                    f"Заработная плата: Зарплата не указана...\n"
                    f"Требования: {re.sub(r'<.*?>', '', self.requirements)}\n"
                    f"Ссылка на вакансию: {self.link}")
        else:
            return (f"\n{"-" * 50}\n\n"
                    f"Название вакансии: {self.name}\n"
                    f"Город: {self.city}\n"
                    f"Заработная плата: {self.salary_from}-{self.salary_to} {self.currency}.\n"
                    f"Требования: {re.sub(r'<.*?>', '', self.requirements) if self.requirements else "Нету"}\n"
                    f"Ссылка на вакансию: {self.link}")

    def __eq__(self, other: object) -> bool:
        """
        Магический метод который проверяет
        равны ли два объекта

        :param other: (object) объект класса с которым сравнивать
        :return: (bool) True | False
        """
        return self.salary_from == other.salary_from

    def __lt__(self, other):
        """
        Магический метод который проверяет
        какой из объектов больше

        :param other: (object) объект класса с которым сравнивать
        :return: (bool) True | False
        """
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        """
        Магический метод который проверяет
        какой из объектов меньше

        :param other: (object) объект класса с которым сравнивать
        :return: (bool) True | False
        """
        return self.salary_from > other.salary_from

    @classmethod
    def cast_to_object_list(cls, vacancies: list[dict, ...] | dict) -> list[object, ...]:
        """
        Класс метод который создает новый объект
        этого класса по полученным данным в поле (vacancies)

        :param vacancies: (list[dict, ...) данные
        :return: (list[object, ...) список объектов
        """
        list_vacancies = []
        # try:
        for vacancy in vacancies:
            name = cls.check_data_str(vacancy['name'])
            if vacancy.get('salary'):
                salary_from = cls.check_data_int(vacancy.get('salary').get('from'))
                salary_to = cls.check_data_int(vacancy.get('salary').get('to'))
                currency = cls.check_data_str(get_currency_transfer(vacancy['salary']['currency']))

            else:
                salary_from = 0
                salary_to = 0
                currency = ''
            city = cls.check_data_str(vacancy['area']['name'])
            requirements = cls.check_data_str(vacancy['snippet']['requirement'])
            link = cls.check_data_str(vacancy['alternate_url'])

            list_vacancies.append(cls(name, city, salary_from, salary_to, currency, requirements, link))

        return list_vacancies

    @staticmethod
    def check_data_str(value):
        "Валидатор для строковых значений "
        if value:
            return value
        return 'информация не найдена'

    @staticmethod
    def check_data_int(value):
        "Валидатор для числовых значений "
        if value:
            return value
        return 0
