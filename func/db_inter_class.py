import psycopg2


class DBManager:
    def __init__(self):
        pass


    def get_companies_and_vacancies_count(self, params) -> str:
        """'Получает список всех компаний и количество вакансий у каждой компании"""

        with psycopg2.connect(database='vacancy_db', **params) as conn:
            conn.autocommit = True
            cur = conn.cursor()

            cur.execute('''SELECT company_name, employee_open_vacancy FROM employee_table''')
            rows = cur.fetchall()
            for row in rows:
                print(f'Компания: {row[0]}, кол-во вакансий: {row[1]} шт')

        cur.close()


    def get_all_vacancies(self, params) -> str:
        """Получает список всех вакансий с указанием названия компании, названия вакансии
        и зарплаты и ссылки на вакансию."""
        with psycopg2.connect(database='vacancy_db', **params) as conn:
            conn.autocommit = True
            cur = conn.cursor()

            cur.execute('''SELECT company_name, vacancy_name, salary_from, salary_to, salary_currency, vacancy_url FROM 
            vacancy_table ORDER BY salary_from DESC''')
            rows = cur.fetchall()
            for i in rows:
                print(f'{i[0]} - {i[1]}, с зарплатой от {i[2]} {i[4]} до {i[3]} {i[4]}, ссылка на вакансию: {i[5]}')

        cur.close()



    def get_avg_salary(self, params) -> str:
        """Получает среднюю зарплату по вакансиям."""
        with psycopg2.connect(database='vacancy_db', **params) as conn:
            conn.autocommit = True
            cur = conn.cursor()

            cur.execute("SELECT AVG((salary_from + salary_to)/2) AS СРЕДНЯЯ_ЗП FROM vacancy_table")

            rows = cur.fetchall()
            for i in rows:
                return i[0]

        cur.close()



    def get_vacancies_with_higher_salary(self, data, params) -> str:
        """Получает список всех вакансий, у которых зарплата выше
        средней по всем вакансиям."""
        with psycopg2.connect(database='vacancy_db', **params) as conn:
            conn.autocommit = True
            cur = conn.cursor()

            cur.execute(f"SELECT vacancy_name, vacancy_url FROM vacancy_table where (salary_to + salary_from/2) > {data}")

            rows = cur.fetchall()
            print('Вакансия с зп выше средней:')
            for i in rows:
                print(f'{i[0]}, ссылка {i[1]}')

        cur.close()


    def get_vacancies_with_keyword(self, key_word, params) -> str:
        """Получает список всех вакансий, в названии которых содержатся переданные
        в метод слова, например python."""
        with psycopg2.connect(database='vacancy_db', **params) as conn:
            conn.autocommit = True
            cur = conn.cursor()

            cur.execute(f"""SELECT vacancy_name FROM vacancy_table WHERE vacancy_name LIKE '%{key_word}%'""")
            rows = cur.fetchall()
            print('Вакансии с ключевым словом:')
            for i in rows:
                print(f'{i[0]}')

        cur.close()