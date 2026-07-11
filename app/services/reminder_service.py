from apscheduler.schedulers.asyncio import AsyncIOScheduler

from sqlalchemy import select

from app.database.db import SessionLocal

from app.database.models import (
    UserSettings,
    Goal
)

from app.utils.calculator import calculate_savings



scheduler = AsyncIOScheduler()



async def send_reminders():

    async with SessionLocal() as session:

        result = await session.execute(

            select(UserSettings)
            .where(
                UserSettings.reminders == True
            )

        )


        users = result.scalars().all()



        for user in users:


            goals_result = await session.execute(

                select(Goal)
                .where(
                    Goal.user_id == user.user_id
                )

            )


            goals = goals_result.scalars().all()


            if not goals:
                continue



            text = "🔔 Ежедневное напоминание\n\n"



            for goal in goals:


                calculation = calculate_savings(

                    goal.target_amount,

                    goal.current_amount,

                    goal.deadline

                )



                text += (

                    f"🎯 {goal.title}\n\n"

                    f"💰 Накоплено:\n"

                    f"{goal.current_amount:.0f} ₽ "
                    f"/ {goal.target_amount:.0f} ₽\n\n"

                )



                if calculation:


                    text += (

                        f"📊 Прогресс:\n"

                        f"{goal.current_amount / goal.target_amount * 100:.1f}%\n\n"

                        f"⏳ Осталось:\n"

                        f"{calculation['days_left']} дней\n\n"

                        f"💵 Сегодня нужно:\n"

                        f"{calculation['per_day']:.0f} ₽\n\n"

                    )


                text += (
                    "🚀 Продолжай двигаться к цели!\n\n"
                )



            try:

                from app.bot_instance import bot


                await bot.send_message(

                    chat_id=user.user_id,

                    text=text

                )


            except Exception as e:

                print(
                    "Ошибка отправки:",
                    e
                )





def start_scheduler():


    scheduler.add_job(

        send_reminders,

        trigger="cron",

        hour=12,

        minute=0

    )


    scheduler.start()