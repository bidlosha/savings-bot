from aiogram import Router
from aiogram.types import Message

from app.database.db import SessionLocal

from app.database.crud import get_goals_with_progress

from app.utils.calculator import calculate_savings



router = Router()



@router.message(
    lambda message:
    message.text == "📋 Мои цели"
)
async def my_goals(
    message: Message
):

    async with SessionLocal() as session:

        goals = await get_goals_with_progress(
            session,
            message.from_user.id
        )


    if not goals:

        await message.answer(
            "📋 У тебя пока нет целей"
        )

        return



    text = "📋 Твои цели:\n\n"



    for goal in goals:


        progress = (

            goal.current_amount /
            goal.target_amount *
            100

        )


        calculation = calculate_savings(

            goal.target_amount,

            goal.current_amount,

            goal.deadline

        )



        text += (

            f"🎯 {goal.title}\n\n"

            f"💰 Накоплено:\n"

            f"{goal.current_amount:.0f} ₽ "
            f"из {goal.target_amount:.0f} ₽\n\n"

            f"📊 Прогресс:\n"

            f"{progress:.1f}%\n\n"

            f"📅 Дата:\n"

            f"{goal.deadline}\n\n"

        )


        if calculation:


            text += (

                f"⏳ Осталось:\n"

                f"{calculation['days_left']} дней\n\n"

                f"Нужно откладывать:\n\n"

                f"💵 В день: "
                f"{calculation['per_day']:.0f} ₽\n"

                f"📆 В неделю: "
                f"{calculation['per_week']:.0f} ₽\n"

                f"📅 В месяц: "
                f"{calculation['per_month']:.0f} ₽\n\n"

            )


        text += "────────────\n\n"



    await message.answer(text)