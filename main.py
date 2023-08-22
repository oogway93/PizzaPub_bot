from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

API_TOKEN = TOKEN

bot = Bot(API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)


async def on_startup(_):
    print("Bot was started")


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer(f'Приветствую вас в PizzaPub')



if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
