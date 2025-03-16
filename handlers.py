from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F
from aiogram.enums import ParseMode





from keyboards import main_keyboard, weather_keyboard, currency_keyboard, vacancies_keyboard
from api.weather_api import get_weather
from api.courses_api import get_courses
from api.vacancies_api import get_vacancies

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я бот, который поможет тебе узнать погоду, курсы валют и вакансии Python.",
        reply_markup=main_keyboard()
    )


@router.message(F.text == "Погода")
async def show_weather_keyboard(message: Message):
    await message.answer("Выберите день для прогноза:", reply_markup=weather_keyboard())

@router.message(F.text == "Погода сегодня")
async def weather_today(message: Message):
    weather = get_weather(0)
    await message.answer(weather, reply_markup=weather_keyboard())

@router.message(F.text == "Погода завтра")
async def weather_tomorrow(message: Message):
    weather = get_weather(1)
    await message.answer(weather, reply_markup=weather_keyboard())

@router.message(F.text == "Погода послезавтра")
async def weather_after_tomorrow(message: Message):
    weather = get_weather(2)
    await message.answer(weather, reply_markup=weather_keyboard())


@router.message(F.text == "Курс валют")
async def show_currency_keyboard(message: Message):
    await message.answer("Выберите валюту:", reply_markup=currency_keyboard())

@router.message(F.text == "Курс RUB")
async def currency_rub(message: Message):
    rate = get_courses("RUB")
    await message.answer(rate, reply_markup=currency_keyboard())

@router.message(F.text == "Курс USD")
async def currency_usd(message: Message):
    rate = get_courses("USD")
    await message.answer(rate, reply_markup=currency_keyboard())

@router.message(F.text == "Курс EUR")
async def currency_eur(message: Message):
    rate = get_courses("EUR")
    await message.answer(rate, reply_markup=currency_keyboard())


@router.message(F.text == "Вакансии Python")
async def show_vacancies_keyboard(message: Message):
    await message.answer("Выберите уровень:", reply_markup=vacancies_keyboard())

@router.message(F.text == "Junior Python")
async def vacancies_junior(message: Message):
    jobs = get_vacancies("Junior")
    await message.answer(jobs, reply_markup=vacancies_keyboard())

@router.message(F.text == "Middle Python")
async def vacancies_middle(message: Message):
    jobs = get_vacancies("Middle")
    await message.answer(jobs, reply_markup=vacancies_keyboard())

@router.message(F.text == "Senior Python")
async def vacancies_senior(message: Message):
    jobs = get_vacancies("Senior")
    await message.answer(jobs, reply_markup=vacancies_keyboard())

@router.message(F.text == "Назад в меню")
async def back_to_menu(message: Message):
    await message.answer("Главное меню:", reply_markup=main_keyboard())

