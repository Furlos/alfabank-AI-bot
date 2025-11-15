from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup




def main_kb(language: str):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=make_request_msg(language), callback_data="start_request")],
        ]
    )
def make_request_msg(language: str):
    messages = {
        "ru": f"""
    Sdelai zapros
    """,
        "en": f"""
    Make request
        """
    }
    return messages.get(language, messages["en"])

def comeback_kb(language: str):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=comeback_msg(language), callback_data="start")],
        ]
    )

def comeback_msg(language: str):
    messages = {
        "ru": f"""
    Vernutsya
    """,
        "en": f"""
    Comeback
        """
    }
    return messages.get(language, messages["en"])