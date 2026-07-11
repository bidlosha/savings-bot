from aiogram import Router
from aiogram.types import Message

from app.database.db import SessionLocal

from app.database.crud import toggle_reminders


router = Router()



@router.message(
    lambda message:
    message.text == "🔔 Напоминания"
)
async def reminders(
    message: Message
):

    async with SessionLocal() as session:

        settings = await toggle_reminders(
            session,
            message.from_user.id
        )


    status = (
        "включены ✅"
        if settings.reminders
        else
        "выключены ❌"
    )


    await message.answer(
        f"🔔 Напоминания {status}"
    )