import asyncio

from aiogram import Bot, Dispatcher

import db
from config import TOKEN
from handlers.handlers import router

API_TOKEN = TOKEN

bot = Bot(API_TOKEN, parse_mode="HTML")
dp = Dispatcher()


async def on_startup():
    print("Bot was started")


async def main():
    dp.include_router(router)
    await db.sql_start_db()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, on_startup=on_startup)


if __name__ == '__main__':
    asyncio.run(main())
