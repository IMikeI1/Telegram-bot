from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main_keyboard():
    weather_btn = KeyboardButton(text='Погода')
    currency_btn = KeyboardButton(text='Курс валют')
    vacancies_btn = KeyboardButton(text='Вакансии Python')

    keyboard = ReplyKeyboardMarkup(
        keyboard=[[weather_btn], [currency_btn], [vacancies_btn]],
        resize_keyboard=True
    )
    return keyboard


def weather_keyboard():
    today_btn = KeyboardButton(text='Погода сегодня')
    tomorrow_btn = KeyboardButton(text='Погода завтра')
    after_tomorrow_btn = KeyboardButton(text='Погода послезавтра')
    back_btn = KeyboardButton(text='Назад в меню')

    keyboard = ReplyKeyboardMarkup(
        keyboard=[[today_btn], [tomorrow_btn], [after_tomorrow_btn], [back_btn]],
        resize_keyboard=True
    )
    return keyboard


def currency_keyboard():
    rub_btn = KeyboardButton(text='Курс RUB')
    usd_btn = KeyboardButton(text='Курс USD')
    eur_btn = KeyboardButton(text='Курс EUR')
    back_btn = KeyboardButton(text='Назад в меню')

    keyboard = ReplyKeyboardMarkup(
        keyboard=[[rub_btn], [usd_btn], [eur_btn], [back_btn]],
        resize_keyboard=True
    )
    return keyboard


def vacancies_keyboard():
    junior_btn = KeyboardButton(text='Junior Python')
    middle_btn = KeyboardButton(text='Middle Python')
    senior_btn = KeyboardButton(text='Senior Python')
    back_btn = KeyboardButton(text='Назад в меню')

    keyboard = ReplyKeyboardMarkup(
        keyboard=[[junior_btn], [middle_btn], [senior_btn], [back_btn]],
        resize_keyboard=True
    )
    return keyboard