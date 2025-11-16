from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def main_kb(language: str):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text=make_request_msg(language),
                callback_data="start_request"
            )],
        ]
    )

def make_request_msg(language: str):
    messages = {
        "ru": "🚀 Сделать бизнес-запрос",
        "en": "🚀 Make business request"
    }
    return messages.get(language, messages["en"])

def comeback_kb(language: str):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text=comeback_msg(language),
                callback_data="start"
            )],
        ]
    )

def comeback_msg(language: str):
    messages = {
        "ru": "🏠 Вернуться в главное меню",
        "en": "🏠 Back to main menu"
    }
    return messages.get(language, messages["en"])