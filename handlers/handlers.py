from aiogram import types, Dispatcher

import db
from keyboards import keyboards
import main
from pizza_data import rest


# @dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await main.bot.send_message(message.from_user.id, 'Приветствую вас в PizzaPub', reply_markup=keyboards.kb)
    await message.delete()
    await main.bot.send_photo(message.from_user.id,
                              "https://popmenucloud.com/hacnfrue/40ce9bb7-a08e-4abd-9926-56ee24b02e07.JPG")


# @dp.message_handler(commands=['Location'])
async def location_handler(message: types.Message):
    await main.bot.send_message(message.from_user.id, text=rest, parse_mode="HTML")
    await message.delete()


# @dp.message_handler(commands=['Schedule'])
async def work_schedule_handler(message: types.Message):
    await main.bot.send_message(message.from_user.id, text="Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00")
    await message.delete()


# @dp.message_handler(commands=['Menu'])
async def menu_handler(message: types.Message):
    await db.sql_read(message)
    await message.delete()


# @dp.callback_query_handler()
async def callback_feedback_pizza(callback: types.CallbackQuery):
    if callback.data == 'Like':
        await callback.answer("Спасибо за ваш хороший отзыв❤️")
    elif callback.data == 'Dislike':
        await callback.answer("Сожалеем, что не оправдали ваших ожиданий.😢 Закажите что-нибудь другое")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(location_handler, commands=['Location'])
    dp.register_message_handler(work_schedule_handler, commands=['Schedule'])
    dp.register_message_handler(menu_handler, commands=['Menu'])
    dp.register_callback_query_handler(callback_feedback_pizza)
