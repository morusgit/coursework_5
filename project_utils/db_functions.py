import json

import psycopg2


def create_database(database_name: str, params: dict) -> None:
    """Создает новую базу данных."""

    conn = psycopg2.connect(database='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f'DROP DATABASE {database_name}')
    cur.execute(f'CREATE DATABASE {database_name}')

    cur.close()
    conn.close()


def execute_sql_script(cur, script_file) -> None:
    """Выполняет скрипт из файла для заполнения БД данными."""

    cur.execute(open(script_file, "r").read())


def read_json_file_vacancy() -> list:
    """чтение файла json для заполнения таблицы vacancy_table"""

    with open(f'vacancies_of_company.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        list_vacancy_for_bd = []
        for vacancy in data['items']:
            name = vacancy['name']
            try:
                salary_from = vacancy["salary"]["from"]
                salary_to = vacancy['salary']["to"]
                currency = vacancy['salary']['currency']
                employee_name = vacancy['employer']['name']
                url = vacancy['alternate_url']
            except TypeError:
                salary_from = 0
                salary_to = 0
                currency = "None"
                employee_name = "None"
                url = "None"

            for_vacancy_list = (name, salary_from, salary_to, currency, employee_name, url)
            list_vacancy_for_bd.append(for_vacancy_list)

        return list_vacancy_for_bd


def read_json_file_employers() -> list:
    """чтение файла json для заполнения таблицы employee_table"""

    with open(f'employers_and_vacancies.json', 'r', encoding='UTF-8') as file:
        data = json.load(file)

        list_employee_for_bd = [(i["id"], i["name"], i["alternate_url"], i["open_vacancies"]) for i in data['items']]
        return list_employee_for_bd


def insert_data_in_vacancy_table(cur, data) -> None:
    """заполняет таблицу vacancy_table данными из json файла"""

    cur.executemany('INSERT INTO vacancy_table(vacancy_name, salary_from, salary_to, salary_currency, company_name, vacancy_url)'
                    'VALUES (%s, %s, %s, %s, %s, %s);', (data))


def insert_data_in_employee_table(cur, data) -> None:
    """заполняет таблицу employee_table данными из json файла"""


    cur.executemany('INSERT INTO employee_table(employee_id, company_name, employee_url, employee_open_vacancy)'
                    'VALUES (%s, %s, %s, %s);', (data))