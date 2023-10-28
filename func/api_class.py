import requests
import json


class Api_requests_about_employers_and_vacancies:

    def __init__(self):
        self.__name = {}

    @property
    def name(self):
        return self.__name

    def get_employers_of_choice_company(self) -> None:
        """Сохраняем в json файл данные о компаниях"""

        params = {
            "per_page": 10,
            'sort_by': "by_vacancies_open",
            'only_with_vacancies': True
        }

        response = requests.get(f'https://api.hh.ru/employers', params).json()
        with open(f'../src/employers_and_vacancies.json', 'w', encoding='utf-8') as file:
            json.dump(response, file, indent=4, ensure_ascii=False)

            self.__name = {item['name']: item['id'] for item in response['items']}

    def get_vacancies_of_choiced_company(self, data) -> None:
        """Сохраняем в json файл данные с вакансиями по выбранном компании"""

        for i in range(21):
            params = {
                'per_page': 100,
                'pages': i
            }
            response = requests.get(f'https://api.hh.ru/vacancies?employer_id={data}', params=params).json()
            with open(f'../src/vacancies_of_company.json', 'w', encoding='utf-8') as file:
                json.dump(response, file, indent=4, ensure_ascii=False)