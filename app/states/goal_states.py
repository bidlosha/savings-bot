from aiogram.fsm.state import (
    State,
    StatesGroup
)


class GoalCreate(StatesGroup):

    title = State()

    amount = State()

    deadline = State()