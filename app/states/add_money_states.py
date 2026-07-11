from aiogram.fsm.state import (
    State,
    StatesGroup
)


class AddMoney(StatesGroup):

    goal_id = State()

    amount = State()