from aiogram import types, Router, F
from aiogram.filters import CommandStart

import db
from keyboards import reply
from pizza_data import rest

router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer('Приветствую вас в PizzaPub', reply_markup=reply.start_btns)
    await message.delete()
    await message.answer_photo("https://popmenucloud.com/hacnfrue/40ce9bb7-a08e-4abd-9926-56ee24b02e07.JPG")


@router.message(F.text.in_(['📜 Рестораны г. Ростов-на-Дону']))
async def location_handler(message: types.Message):
    await message.answer(text=rest)
    await message.delete()


@router.message(F.text.in_(['🗓 График работы']))
async def work_schedule_handler(message: types.Message):
    await message.answer(text="Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00")
    await message.delete()


@router.message(F.text.in_(['🍕 Меню']))
async def menu_handler(message: types.Message):
    await db.sql_read(message)
    await message.delete()


@router.callback_query()
async def callback_feedback_pizza(callback: types.CallbackQuery):
    answers = {'Like': "Спасибо, мы старались с готовкой❤️",
               'Dislike': "Сожалеем, что не оправдали ваших ожиданий😢"}
    await callback.answer(answers[f"{callback.data}"])
