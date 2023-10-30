from aiogram import types, Router, F
from aiogram.filters import CommandStart

import db
import keyboards
from pizza_data import rest

router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer('Приветствую вас в PizzaPub', reply_markup=keyboards.reply.reply_btns)
    await message.delete()
    await message.answer_photo("https://popmenucloud.com/hacnfrue/40ce9bb7-a08e-4abd-9926-56ee24b02e07.JPG")


@router.message(F.text.lower().in_(['location', 'локация']))
async def location_handler(message: types.Message):
    await message.answer(text=rest)
    await message.delete()


@router.message(F.text.lower().in_(['schedule', 'расписание', 'расписание работы']))
async def work_schedule_handler(message: types.Message):
    await message.answer(text="Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00")
    await message.delete()


@router.message(F.text.lower().in_(['menu', 'меню', 'пицца']))
async def menu_handler(message: types.Message):
    await db.sql_read(message)
    await message.delete()


@router.callback_query()
async def callback_feedback_pizza(callback: types.CallbackQuery):
    if callback.data == 'Like':
        await callback.answer("Спасибо за ваш хороший отзыв❤️")
    elif callback.data == 'Dislike':
        await callback.answer("Сожалеем, что не оправдали ваших ожиданий😢")
