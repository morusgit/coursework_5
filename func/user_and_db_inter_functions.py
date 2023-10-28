from func.api_class import Api_requests
from func.db_inter_class import DBManager
from config import config
from func.db_functions import create_database, execute_sql_script, read_json_file_employers, read_json_file_vacancy
from func.db_functions import insert_data_in_vacancy_table, insert_data_in_employee_table
import psycopg2


def database_interaction() -> None:
    """взаимодействия с БД: создание БД, таблиц, заполнение таблиц данными из json файлов"""

    db_name = 'vacancy_db'
    script_file = 'vacancy.sql'

    params = config()
    conn = None

    create_database(db_name, params)

    params.update({'dbname': db_name})
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                execute_sql_script(cur, script_file)

                employee_data = read_json_file_employers()
                insert_data_in_employee_table(cur, employee_data)
                vacancy_data = read_json_file_vacancy()
                insert_data_in_vacancy_table(cur, vacancy_data)

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()



def user_interaction(params):
    """Взаимодействие с пользователем и создание vacancy-table таблицы с указанием ID компании """

    class_api_exemp = Api_requests()
    class_api_exemp.get_employers_of_choice_company()

    data = class_api_exemp.name

    print(f"""Напиши название компании из списка, по которой ты бы хотел получить информацию о вакансиях:\n""")

    print('\n'.join([k for k in data.keys()]))
    user_choice = input('>>> ')

    if user_choice in data.keys():
        class_api_exemp.get_vacancies_of_choiced_company(data.get(user_choice))

    else:
        print("В выборке данной компании нет")

def user_inter_with_class_DBManager(params):
    db_class_exemp = DBManager()

    #user_number = 0
    #while user_number < 5:
    while True:
        print('\n'
              'Выбери из списка какие данные ты бы хотел получить, укажи цифру:\n'
              '1 - Получение списка всех компанией и кол-ва вакансий\n'
              '2 - Получение списка всех вакансий выбранной компании с ЗП и с ссылкой\n'
              '3 - Получение средней зарплаты по выбранной компании\n'
              '4 - Получение всех вакансий у которых ЗП выше средней\n'
              '5 - Получение списка вакансий с ключевым словом\n'
              'exit - выход из программы\n')
        user_choice = int(input())
        if user_choice == 1:
            db_class_exemp.get_companies_and_vacancies_count(params)

        elif user_choice == 2:
            db_class_exemp.get_all_vacancies(params)

        elif user_choice == 3:
            print(db_class_exemp.get_avg_salary(params))

        elif user_choice == 4:
            db_class_exemp.get_vacancies_with_higher_salary(db_class_exemp.get_avg_salary(params), params)

        elif user_choice == 5:
            user_key_word = str(input("Наберите ключевое слово: "))
            db_class_exemp.get_vacancies_with_keyword(user_key_word, params)

        elif user_choice == 'exit':
            break


