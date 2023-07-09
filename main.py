from utils import *  # Импортирование всех имен из модуля utils
from src.save_info_in_JSON_file import JSONSaver


def main():
    one_more_search()  # Вызов функции one_more_search для выполнения первого поиска вакансий

    info_work = JSONSaver()  # Создание экземпляра класса JSONSaver и присвоение его переменной info_work

    salary_range = input('Введите диапазон зарплат через пробел (например, "10000 50000"): ')

    # Вызов метода get_vacancies_by_salary у объекта info_work и сохранение результата в переменной salary_list
    salary_list = info_work.get_vacancies_by_salary(salary_range)

    # Сортировка списка salary_list по ключу 'salary_from' в порядке убывания и сохранение в переменной sorted_list
    sorted_list = sorted(salary_list, key=lambda x: x['salary_from'], reverse=True)

    if sorted_list:  # Проверка, содержит ли sorted_list вакансии
        top_n = int(input('Введите количество вакансий для вывода в топ N: '))

        # Получение списка top_vacancies, содержащего топ N вакансий из sorted_list
        top_vacancies = get_top_vacancies(sorted_list, top_n)

        print('=====================================================================')

        # Вывод информации о вакансиях в удобочитаемом формате с помощью функции return_beautifully_vacancies
        return_beautifully_vacancies(top_vacancies)

    else:
        print('Нет вакансий, соответствующих данному диапазону.\n')

    while True:
        if input('Продолжить? (да/нет)\n').lower() in ['lf', 'да']:
            print('Действия: \n'
                  '1)Вывод всех отсортированных вакансий\n'
                  '2)Удалить вакансию по ID\n'
                  '3)Произвести повторный поиск вакансий\n'
                  '4)Отсортировать еще раз(если Вы добавили еще вакансии или хотите отсортировать по новым значениям)')
        else:
            print('Спасибо! Надеюсь, Вы нашли подходящую вакансию!')
            break

        next_move = int(input())
        if next_move == 1:
            for vacancy in sorted_list:
                print(vacancy)  # Вывод информации о каждой вакансии из sorted_list

        elif next_move == 2:
            delete_vacancy = input('Введите ID вакансии, которую вы хотите убрать: ')
            info_work.delete_vacancy(
                int(delete_vacancy))  # Вызов метода delete_vacancy у info_work для удаления вакансии по указанному ID
            sorted_list = [vacancy for vacancy in sorted_list if vacancy.get('vacancy_id') != delete_vacancy]
            print('Вакансия убрана!\n')

        elif next_move == 3:
            # Вызов функции choose_platform для повторного поиска вакансий на другой платформе
            choose_platform()

        elif next_move == 4:
            salary_range = input('Введите новый диапазон зарплат через пробел: ')

            # Получение нового списка вакансий по указанному диапазону зарплат
            salary_list = info_work.get_vacancies_by_salary(salary_range)

            sorted_list = sorted(salary_list, key=lambda x: x['salary_from'], reverse=True)
            top_n = int(input('Введите количество вакансий для вывода в топ N: '))
            top_vacancies = sorted_list[:top_n]  # Получение нового списка top_vacancies с топ N вакансиями

            print('=====================================================================')

            # Вывод информации о вакансиях в удобочитаемом формате с помощью функции return_beautifully_vacancies
            return_beautifully_vacancies(top_vacancies)

        else:
            print('Спасибо! Надеюсь, Вы нашли подходящую вакансию!')


if __name__ == '__main__':
    main()
