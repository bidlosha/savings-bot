from datetime import datetime



def calculate_savings(
    target_amount,
    current_amount,
    deadline
):

    try:

        deadline_date = datetime.strptime(
            deadline,
            "%d.%m.%Y"
        )


    except ValueError:

        return None



    today = datetime.now()


    days_left = (
        deadline_date - today
    ).days



    if days_left <= 0:

        days_left = 1



    remaining = (
        target_amount -
        current_amount
    )


    if remaining < 0:

        remaining = 0



    per_day = (
        remaining /
        days_left
    )


    per_week = (
        per_day *
        7
    )


    per_month = (
        per_day *
        30
    )


    return {

        "days_left": days_left,

        "remaining": remaining,

        "per_day": per_day,

        "per_week": per_week,

        "per_month": per_month

    }