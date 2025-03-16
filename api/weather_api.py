import requests
from datetime import datetime, timedelta



def get_weather(day_offset=0):
    try:
        weather_data = {
            0: {
                "temp": "0°",
                "feels_like": "-7°",
                "condition": "снег",
                "wind": "6.5 м/с",
                "pressure": "748 мм.рт.ст",
                "humidity": "88%"
            },
            1: {
                "temp": "-1°",
                "feels_like": "-8°",
                "condition": "снег",
                "wind": "6 м/с",
                "pressure": "751 мм.рт.ст",
                "humidity": "66%"
            },
            2: {
                "temp": "-5°",
                "feels_like": "-11°",
                "condition": "ясно",
                "wind": "4.1 м/с",
                "pressure": "757 мм.рт.ст",
                "humidity": "73%"
            }
        }

        data = weather_data.get(day_offset, {})
        if not data:
            return "Данные о погоде недоступны"

        date = datetime.now() + timedelta(days=day_offset)
        date_str = date.strftime("%d.%m.%Y")

        return (f"Прогноз погоды на {date_str}:\n"
                f"Температура: {data['temp']}\n"
                f"Ощущается как: {data['feels_like']}\n"
                f"Условия: {data['condition']}\n"
                f"Ветер: {data['wind']}\n"
                f"Давление: {data['pressure']}\n"
                f"Влажность: {data['humidity']}")

    except Exception as e:
        return f"Ошибка при получении данных о погоде: {str(e)}"