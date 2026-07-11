from aiogram import Bot
from aiogram import Dispatcher

from app.config import BOT_TOKEN
from app.database.db import init_db

from app.handlers import start
from app.handlers import add_money
from app.handlers import goals
from app.handlers import view_goals
from app.handlers import progress
from app.handlers import reminders

from app.bot_instance import bot as bot_instance

from app import bot_instance as bot_storage

from app.services.reminder_service import start_scheduler



async def start_bot():

    print("Создание базы данных...")

    await init_db()


    bot = Bot(
        token=BOT_TOKEN
    )


    # сохраняем бота для отправки напоминаний

    bot_storage.bot = bot



    dp = Dispatcher()



    # Команда /start

    dp.include_router(
        start.router
    )


    # Добавление накоплений

    dp.include_router(
        add_money.router
    )


    # Создание целей

    dp.include_router(
        goals.router
    )


    # Просмотр целей

    dp.include_router(
        view_goals.router
    )


    # Прогресс

    dp.include_router(
        progress.router
    )


    # Напоминания

    dp.include_router(
        reminders.router
    )


    # Запуск ежедневных напоминаний

    start_scheduler()



    print("✅ Бот запущен")


    await dp.start_polling(bot)