from src.API_work import HeadHunterAPI, SuperJobAPI


def headhunter_vacancies_search():
    """Функция для обращения к классу HeadHunterAPI для поиска вакансий"""
    hh_api = HeadHunterAPI()  # Создание экземпляра класса HeadHunterAPI
    keywords = input('Введите запрос через пробел, а также город поиска вакансии: ')
    vacancy_quantity = int(input('Введите количество вакансий: '))
    searched_vacancies = hh_api.get_vacancies(keywords, vacancy_quantity)  # Получение списка найденных вакансий
    hh_api.get_vacancies_info(searched_vacancies)  # Вывод информации о найденных вакансиях


def superjob_vacancies_search():
    """Функция для обращения к классу SuperJobAPI для поиска вакансий"""
    sj_api = SuperJobAPI()  # Создание экземпляра класса SuperJobAPI
    search_query = input('Введите запрос через пробел, а также город поиска вакансии: ')
    vacancy_quantity = int(input('Введите количество вакансий: '))
    searched_vacancies = sj_api.get_vacancies(search_query, vacancy_quantity)  # Получение списка найденных вакансий
    sj_api.get_vacancies_info(searched_vacancies)  # Вывод информации о найденных вакансиях


def choose_platform():
    """Запрос у пользователя выбор платформы для поиска вакансий и вызов соответствующей функции для поиска"""
    platforms = input('Выберите платформу для поиска вакансии: HeadHunter или SuperJob? ').lower()
    if platforms in ['хедхантер', 'хэдхантер', 'хх', 'headhunter', 'hh', '[tl[fynth', '[[', 'рр', 'руфвргтеук', '1']:
        headhunter_vacancies_search()  # Вызов функции для поиска вакансий на HeadHunter
    elif platforms in ['superjob', 'sj', 'суперджоб', 'супержоб', 'сд', 'сж', 'ыгзукощи', 'ыо', 'cl', 'c;', '2']:
        superjob_vacancies_search()  # Вызов функции для поиска вакансий на SuperJob


def one_more_search():
    """Выполняет повторный поиск вакансий на другой платформе по желанию пользователя"""
    choose_platform()
    second_platform = input('Хотите посмотреть еще на другой платформе? (да/нет)? ').lower()
    if second_platform in ['да', 'lf', 'yes', 'нуы']:
        choose_platform()  # Выбор и поиск вакансий на другой платформе, если пользователь желает


def get_top_vacancies(sorted_vac_list, last_vacancy=10000):
    """Возвращает last_vacancy самых популярных вакансий из отсортированного списка sorted_vac_list"""
    if last_vacancy <= len(sorted_vac_list):
        beginning = sorted_vac_list[:last_vacancy]  # Выбор указанного количества вакансий из начала списка
        return beginning
    else:
        return sorted_vac_list


def return_beautifully_vacancies(sorted_vac_list):
    """Выводит информацию о вакансиях в удобочитаемом формате."""
    for vac in sorted_vac_list:
        for k, v in vac.items():
            print(f'{k} - {v}')  # Вывод информации о вакансии в удобочитаемом формате
        print('===============================================')
