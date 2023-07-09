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
