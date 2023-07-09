from abc import ABC, abstractmethod
import json


class JSON(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy: dict):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, salary_range='0 0'):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_id: int):
        pass


class JSONSaver(JSON):
    def add_vacancy(self, vacancy: dict) -> None:
        """Добавляет вакансию в список и сохраняет его в JSON файл."""
        with open('fav_vacancies.json', 'a', encoding='utf-8') as file:
            json.dump(vacancy, file, ensure_ascii=False)
            file.write('\n')  # Добавляем символ новой строки после каждой записи

    def get_vacancies_by_salary(self, salary_range='0 0'):
        """Возвращает вакансии, отфильтрованные по зарплате."""
        filtered_vacs = []
        salary_filter = salary_range.split()
        salary_min, salary_max = map(int, salary_filter)

        with open('fav_vacancies.json', 'r', encoding='utf-8') as file:
            all_info = [json.loads(line) for line in file]  # Загружаем каждую строку как отдельный JSON объект

            for vacancy in all_info:
                salary_from = vacancy.get('salary_from')
                salary_to = vacancy.get('salary_to')

                if (salary_from is not None and salary_min <= salary_from <= salary_max) or \
                        (salary_to is not None and salary_min <= salary_to <= salary_max):
                    filtered_vacs.append(vacancy)

        return filtered_vacs

    def delete_vacancy(self, vacancy_id: int):
        """Удаляет вакансию из списка в JSON файле по 'vacancy_id' и перезаписывает список."""
        with open('fav_vacancies.json', 'r', encoding='utf-8') as file:
            data = [json.loads(line) for line in file]

        new_data = [vacancy for vacancy in data if vacancy.get('vacancy_id') != vacancy_id]

        with open('fav_vacancies.json', 'w', encoding='utf-8') as file:
            for vacancy in new_data:
                json.dump(vacancy, file, ensure_ascii=False)
                file.write('\n')
