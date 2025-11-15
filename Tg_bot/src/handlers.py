from aiogram import Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from messages import start_message, info_message, main_menu_message
from keyboards import make_request_msg, main_kb, comeback_kb
from api import make_request

main_router = Router()

class RequestStates(StatesGroup):
    waiting_for_request = State()

@main_router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        text=start_message(message.from_user.username, message.from_user.language_code),
        reply_markup=main_kb(message.from_user.language_code)
    )

@main_router.callback_query(F.data == "start_request")
async def start_request_handler(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(RequestStates.waiting_for_request)
    await callback.message.edit_text(
        text=info_message(callback.from_user.language_code),
        reply_markup=comeback_kb(callback.from_user.language_code)
    )
    await callback.answer()

@main_router.callback_query(F.data == "start")
async def comeback_handler(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text(
        text=main_menu_message(callback.from_user.language_code),
        reply_markup=main_kb(callback.from_user.language_code)
    )
    await callback.answer()

@main_router.message(StateFilter(RequestStates.waiting_for_request))
async def make_request_handler(message: types.Message, state: FSMContext):
    await state.clear()
    response_text = await make_request(message.text)
    await message.answer(
        text=response_text,
        reply_markup=comeback_kb(message.from_user.language_code)
    )