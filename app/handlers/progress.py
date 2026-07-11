from aiogram import Router
from aiogram.types import Message

from app.database.db import SessionLocal
from app.database.crud import get_goals_with_progress


router = Router()


@router.message(
    lambda message: message.text == "📈 Прогресс"
)
async def progress(message: Message):

    async with SessionLocal() as session:

        goals = await get_goals_with_progress(
            session,
            message.from_user.id
        )


    if not goals:

        await message.answer(
            "📈 Активных целей нет"
        )

        return


    text = "📈 Твой прогресс:\n\n"


    for goal in goals:

        percent = (
            goal.current_amount /
            goal.target_amount *
            100
        )


        remaining = (
            goal.target_amount -
            goal.current_amount
        )


        text += (
            f"🎯 {goal.title}\n"
            f"📊 {percent:.1f}%\n"
            f"💰 Осталось: {remaining:.0f} ₽\n\n"
        )


    await message.answer(text)