from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.keyboards.main_menu import main_menu


router = Router()



@router.message(CommandStart())
async def start_handler(
    message: Message
):

    await message.answer(

        "💰 Добро пожаловать в бот накоплений!\n\n"
        "Я помогу тебе создать цель и "
        "рассчитать путь к ней.",

        reply_markup=main_menu

    )