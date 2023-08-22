from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Command
import db


from config import TOKEN
import keyboards

API_TOKEN = TOKEN

bot = Bot(API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

rest = """<b><i>Ростов-на-Дону</i></b>\n<u>ул. Таганрогская, 112/6</u>\n<u>пр-т Ленина, 99</u>\n<u>ул. Пушкинская, 169</u>\n<u>ул. Волкова, 9б</u>\n<u>пр-т Сельмаш, 9</u>\n<u>пр-т Буденновский, 19а/55</u>"""


async def on_startup(_):
    print("Bot was started")


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, 'Приветствую вас в PizzaPub', reply_markup=keyboards.kb)
    await message.delete()
    await bot.send_photo(message.from_user.id,
                         "https://popmenucloud.com/hacnfrue/40ce9bb7-a08e-4abd-9926-56ee24b02e07.JPG")


@dp.message_handler(commands=['Location'])
async def situation_handler(message: types.Message):
    await bot.send_message(message.from_user.id, text=rest, parse_mode="HTML")


@dp.message_handler(commands=['Schedule'])
async def work_schedule_handler(message: types.Message):
    await bot.send_message(message.from_user.id, text="Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00")


@dp.message_handler(commands=['Menu'])
async def menu_handler(message: types.Message):
    await db.sql_read(message)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
