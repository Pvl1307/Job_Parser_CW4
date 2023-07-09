from abc import ABC, abstractmethod  # Для абстракции классов
import requests  # Модуль для работы с HTTP-запросами.
import os  # Модуль для работы с операционной системой. Для переменной окружения(апи-ключ)


class API(ABC):

    @abstractmethod
    def get_vacancies(self, keyword: str, quantity: int):
        """Подключение к API и получение вакансий"""
        pass

    @abstractmethod
    def get_vacancies_info(self, vacancies: list):
        """Разбор вакансии на составляющие"""
        pass


class HeadHunterAPI(API):
    """Класс для поиска на HH API"""
    url_hh = 'https://api.hh.ru/vacancies/'

    def get_vacancies(self, keyword: str, quantity: int):
        """
        Получает вакансии с платформы HH по ключевому слову.
        Возвращает результат в виде словаря (JSON).
        """
        hh_response = requests.get(self.url_hh, params={
            'text': keyword,  # Ключевое слово для поиска вакансий
            'per_page': quantity,  # Кол-во вакансий
            'only_with_salary': 'true',  # Флаг для получения только вакансий с указанной зарплатой
        })

        vacancies = hh_response.json().get('items')

        return vacancies

    def get_vacancies_info(self, vacancies: list):
        """
        Получает информацию о вакансиях с платформы HH.
        """
        for vacancy in vacancies:
            vacancy_id = vacancy.get("id")  # ID вакансии
            title = vacancy.get('name')  # Название вакансии
            vacancy_url = vacancy.get('alternate_url')  # Ссылка на вакансию
            company_name = vacancy.get('employer').get('name')  # Название компании
            work_area = vacancy.get('area').get('name')  # Регион работы
            salary_from = vacancy.get('salary').get('from')  # Зарплата от
            salary_to = vacancy.get('salary').get('to')  # Зарплата до
            salary_currency = vacancy.get('salary').get('currency')  # Валюта зарплаты

            if salary_from is None or salary_from == 0:
                salary_from = salary_to
            if salary_to is None or salary_to == 0:
                salary_to = salary_from


class SuperJobAPI(API):
    """Класс для работы с SuperJob API"""
    api_key: str = os.getenv('SJ_API_KEY')  # Получаем ключ API SuperJob из переменной окружения

    def get_vacancies(self, keyword: str, quantity: int):
        """
        Получает вакансии с платформы SuperJob по ключевому слову.
        Возвращает результат в виде словаря (JSON).
        """
        sj_response = requests.get(
            'https://api.superjob.ru/2.0/vacancies/',
            headers={'X-Api-App-Id': self.api_key},  # Заголовок с ключом API
            params={
                'keyword': keyword,  # Ключевое слово для поиска вакансий
                'count': quantity,  # Количество вакансий
                'payment_from': 1000  # Минимальная зарплата
            }
        )
        vacancies = sj_response.json().get('objects')

        return vacancies

    def get_vacancies_info(self, vacancies: list):
        """
        Получает информацию о вакансиях с платформы SuperJob.
        """
        for vacancy in vacancies:
            vacancy_id = vacancy.get('id')  # ID вакансии
            title = vacancy.get('profession')  # Название вакансии
            vacancy_url = vacancy.get('link')  # Ссылка на вакансию
            company_name = vacancy.get('client').get('title')  # Название компании
            work_area = vacancy.get('town').get('title')  # Регион работы
            salary_from = vacancy.get('payment_from')  # Зарплата от
            salary_to = vacancy.get('payment_to')  # Зарплата до
            salary_currency = vacancy.get('currency')  # Валюта зарплаты

            if salary_from is None or salary_from == 0:
                salary_from = salary_to
            if salary_to is None or salary_to == 0:
                salary_to = salary_from
