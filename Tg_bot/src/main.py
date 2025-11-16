import asyncio

from aiogram import Bot, Dispatcher
from config import token
from handlers import main_router


async def main():
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(main_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

###Проверка