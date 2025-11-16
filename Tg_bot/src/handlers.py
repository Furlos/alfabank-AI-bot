from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import random

from messages import start_message, info_message, main_menu_message, wait_message
from keyboards import make_request_msg, main_kb, comeback_kb
from api import make_request

main_router = Router()

# Список случайных картинок для теста (можно заменить на свои URL)
RANDOM_IMAGES = [
    "https://t.me/fotos_alpha/2",
    "https://t.me/fotos_alpha/3",
    "https://t.me/fotos_alpha/4",
    "https://t.me/fotos_alpha/5",
    "https://t.me/fotos_alpha/6",
    "https://t.me/fotos_alpha/7"
]


class RequestStates(StatesGroup):
    waiting_for_request = State()


@main_router.message(Command("start"))
async def start_handler(message: types.Message):
    # Выбираем случайную картинку
    random_image = random.choice(RANDOM_IMAGES)

    # Отправляем фото с сообщением
    await message.answer_photo(
        photo=random_image,
        caption=start_message(message.from_user.username, message.from_user.language_code),
        reply_markup=main_kb(message.from_user.language_code)
    )


@main_router.callback_query(F.data == "start_request")
async def start_request_handler(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(RequestStates.waiting_for_request)

    # Выбираем случайную картинку
    random_image = random.choice(RANDOM_IMAGES)

    # Редактируем текущее сообщение, добавляя фото
    await callback.message.edit_media(
        media=types.InputMediaPhoto(
            media=random_image,
            caption=info_message(callback.from_user.language_code)
        ),
        reply_markup=comeback_kb(callback.from_user.language_code)
    )
    await callback.answer()


@main_router.callback_query(F.data == "start")
async def comeback_handler(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()

    # Выбираем случайную картинку для главного меню
    random_image = random.choice(RANDOM_IMAGES)

    # Редактируем текущее сообщение на главное меню с фото
    await callback.message.edit_media(
        media=types.InputMediaPhoto(
            media=random_image,
            caption=main_menu_message(callback.from_user.language_code)
        ),
        reply_markup=main_kb(callback.from_user.language_code)
    )
    await callback.answer()


@main_router.message(StateFilter(RequestStates.waiting_for_request))
async def make_request_handler(message: types.Message, state: FSMContext):
    # Сначала отправляем сообщение "ожидайте"
    wait_msg = await message.answer(
        text=wait_message(message.from_user.language_code)
    )

    await state.clear()

    # Получаем ответ от API
    response_text = await make_request(message.text)

    # Редактируем сообщение "ожидайте" на результат
    await wait_msg.edit_text(
        text=response_text,
        reply_markup=comeback_kb(message.from_user.language_code)
    )