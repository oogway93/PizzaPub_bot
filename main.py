from aiogram import Bot, Dispatcher
from aiogram.utils import executor
import db

from config import TOKEN
from handlers import handlers

API_TOKEN = TOKEN

bot = Bot(API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)


async def on_startup(_):
    print("Bot was started")


handlers.register_handlers(dp)

if __name__ == '__main__':
    db.sql_start_db()
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
