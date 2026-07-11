from sqlalchemy import select

from app.database.models import (
    Goal,
    Transaction,
    UserSettings
)



async def create_goal(
    session,
    user_id,
    title,
    amount,
    deadline
):

    goal = Goal(
        user_id=user_id,
        title=title,
        target_amount=amount,
        deadline=deadline
    )

    session.add(goal)

    await session.commit()

    await session.refresh(goal)

    return goal



async def get_user_goals(
    session,
    user_id
):

    result = await session.execute(

        select(Goal)
        .where(
            Goal.user_id == user_id
        )

    )

    return result.scalars().all()



async def add_money(
    session,
    goal_id,
    amount
):

    result = await session.execute(

        select(Goal)
        .where(
            Goal.id == goal_id
        )

    )


    goal = result.scalar_one()


    goal.current_amount += amount


    transaction = Transaction(
        goal_id=goal_id,
        amount=amount
    )


    session.add(transaction)


    await session.commit()


    return goal



async def get_goals_with_progress(
    session,
    user_id
):

    result = await session.execute(

        select(Goal)
        .where(
            Goal.user_id == user_id
        )

    )

    goals = result.scalars().all()


    return goals



async def get_user_settings(
    session,
    user_id
):

    result = await session.execute(

        select(UserSettings)
        .where(
            UserSettings.user_id == user_id
        )

    )

    settings = result.scalar_one_or_none()


    if not settings:

        settings = UserSettings(
            user_id=user_id,
            reminders=True
        )

        session.add(settings)

        await session.commit()

        await session.refresh(settings)


    return settings



async def toggle_reminders(
    session,
    user_id
):

    settings = await get_user_settings(
        session,
        user_id
    )


    settings.reminders = not settings.reminders


    await session.commit()


    return settings