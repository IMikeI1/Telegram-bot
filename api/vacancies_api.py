import requests


def get_vacancies(level="all"):
    try:
        base_url = "https://api.hh.ru/vacancies"

        params = {
            "text": f"Python {level}",
            "area": 2,
            "per_page": 5,
            "page": 0
        }

        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        result = f"Найдено вакансий Python {level}: {data['found']}\n\n"
        for item in data['items'][:5]:
            salary = "Зарплата не указана"
            if item['salary']:
                if item['salary']['from'] and item['salary']['to']:
                    salary = f"Зарплата: {item['salary']['from']} - {item['salary']['to']} {item['salary']['currency']}"
                elif item['salary']['from']:
                    salary = f"Зарплата от: {item['salary']['from']} {item['salary']['currency']}"
                elif item['salary']['to']:
                    salary = f"Зарплата до: {item['salary']['to']} {item['salary']['currency']}"

            result += f" {item['name']}\n"
            result += f" {item['employer']['name']}\n"
            result += f" {salary}\n"
            result += f" {item['alternate_url']}\n\n"

        return result

    except Exception as e:
        return f"Ошибка при получении вакансий: {str(e)}"
