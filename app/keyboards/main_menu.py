from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)


main_menu = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(
                text="➕ Новая цель"
            )
        ],

        [
            KeyboardButton(
                text="📋 Мои цели"
            )
        ],

        [
            KeyboardButton(
                text="📈 Прогресс"
            )
        ],

        [
            KeyboardButton(
                text="💰 Добавить накопление"
            )
        ],

        [
            KeyboardButton(
                text="🔔 Напоминания"
            )
        ],

        [
            KeyboardButton(
                text="⚙️ Настройки"
            )
        ]

    ],
    resize_keyboard=True
)