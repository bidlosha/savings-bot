from aiogram import Router
from aiogram.types import Message

from aiogram.fsm.context import FSMContext

from app.states.add_money_states import AddMoney

from app.database.db import SessionLocal

from app.database.crud import (
    get_user_goals,
    add_money
)


router = Router()



@router.message(
    lambda message:
    message.text == "💰 Добавить накопление"
)
async def start_add_money(
    message: Message,
    state: FSMContext
):

    async with SessionLocal() as session:

        goals = await get_user_goals(
            session,
            message.from_user.id
        )


    if not goals:

        await message.answer(
            "Сначала создай цель"
        )

        return


    text = "Выбери цель:\n\n"


    for goal in goals:

        text += (
            f"{goal.id}. {goal.title}\n"
        )


    await state.set_state(
        AddMoney.goal_id
    )


    await message.answer(text)



@router.message(
    AddMoney.goal_id
)
async def select_goal(
    message: Message,
    state: FSMContext
):

    await state.update_data(
        goal_id=int(message.text)
    )


    await state.set_state(
        AddMoney.amount
    )


    await message.answer(
        "💰 Введи сумму накопления:"
    )



@router.message(
    AddMoney.amount
)
async def save_money(
    message: Message,
    state: FSMContext
):

    data = await state.get_data()


    amount = float(message.text)


    async with SessionLocal() as session:

        await add_money(

            session,

            data["goal_id"],

            amount

        )


    await state.clear()


    await message.answer(

        f"✅ Добавлено {amount:.0f} ₽"

    )