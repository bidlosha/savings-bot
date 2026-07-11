from aiogram import Router
from aiogram.types import Message

from aiogram.fsm.context import FSMContext


from app.states.goal_states import GoalCreate

from app.database.db import SessionLocal

from app.database.crud import create_goal



router = Router()



@router.message(
    lambda message:
    message.text == "➕ Новая цель"
)
async def start_goal(
    message: Message,
    state: FSMContext
):

    await state.set_state(
        GoalCreate.title
    )


    await message.answer(
        "🎯 Напиши название цели:"
    )



@router.message(
    GoalCreate.title
)
async def get_title(
    message: Message,
    state: FSMContext
):

    await state.update_data(
        title=message.text
    )


    await state.set_state(
        GoalCreate.amount
    )


    await message.answer(
        "💰 Сколько нужно накопить?"
    )



@router.message(
    GoalCreate.amount
)
async def get_amount(
    message: Message,
    state: FSMContext
):

    await state.update_data(
        amount=float(message.text)
    )


    await state.set_state(
        GoalCreate.deadline
    )


    await message.answer(
        "📅 К какой дате накопить?\n"
        "Например: 01.06.2027"
    )



@router.message(
    GoalCreate.deadline
)
async def get_deadline(
    message: Message,
    state: FSMContext
):

    data = await state.get_data()


    async with SessionLocal() as session:

        await create_goal(

            session=session,

            user_id=message.from_user.id,

            title=data["title"],

            amount=data["amount"],

            deadline=message.text

        )


    await state.clear()


    await message.answer(

        "✅ Цель создана!\n\n"

        f"🎯 {data['title']}\n"

        f"💰 {data['amount']} ₽\n"

        f"📅 {message.text}"

    )