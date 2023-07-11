class Vacancy:

    def __init__(self, vacancy_id: int, title: str, vacancy_url: str, company_name: str, work_area: str,
                 salary_from: int, salary_to: int, salary_currency: str) -> None:
        self.vacancy_id = vacancy_id  # ID вакансии
        self.title = title  # Название вакансии
        self.vacancy_url = vacancy_url  # Ссылка на вакансию
        self.company_name = company_name  # Название компании
        self.work_area = work_area  # Регион работы
        self.salary_from = salary_from  # Зарплата от
        self.salary_to = salary_to  # Зарплата до
        self.salary_currency = salary_currency  # Валюта зарплаты

        self.vac_info = dict(vacancy_id=self.vacancy_id, title=self.title, vacancy_url=vacancy_url,
                             company_name=self.company_name, work_area=self.work_area,
                             salary_from=self.salary_from, salary_to=self.salary_to,
                             salary_currency=self.salary_currency)

    def _validate_salary(self):
        """Проверяет, является ли значение переменной salary_from целым числом и больше или равным нулю."""
        return isinstance(self.salary_from, (int, float)) and self.salary_from >= 0

    def __str__(self):
        """Возвращает строковое представление объекта."""
        return f'ID вакансии:  {self.vacancy_id}\n' \
               f'Вакансия:     {self.title}\n' \
               f'Ссылка:       {self.vacancy_url}\n' \
               f'Имя компании: {self.company_name}\n' \
               f'Город работы: {self.work_area}\n' \
               f'Зарплата:     {self.salary_from} {self.salary_currency} - {self.salary_to} {self.salary_currency}\n'

    def __eq__(self, other):
        """Проверяет, равны ли объект self и объект other по значению атрибута 'salary_from'."""
        return self.salary_to == other.salary_to

    def __lt__(self, other):
        """Сравнивает объект self с объектом other на основе значения атрибута 'salary_from'."""
        return self.salary_to < other.salary_to

    def __gt__(self, other):
        return self.salary_to > other.salary_to
