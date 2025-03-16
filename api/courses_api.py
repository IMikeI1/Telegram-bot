import requests



def get_courses(currency_type="all"):
    try:
        rates = {
            "USD": "91.45",
            "EUR": "99.90",
            "RUB": "70.00"
        }

        if currency_type.upper() in rates:
            return f"Курс {currency_type.upper()}: {rates[currency_type.upper()]} ₽"
        elif currency_type == "all":
            return "\n".join([f"Курс {cur}: {rate} ₽" for cur, rate in rates.items()])
        else:
            return "Неизвестная валюта"

    except Exception as e:
        return f"Ошибка при получении курсов валют: {str(e)}"