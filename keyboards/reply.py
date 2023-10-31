from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_btns = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🗓 График работы'),
            KeyboardButton(text='📜 Рестораны г. Ростов-на-Дону'),
        ],
        [
            KeyboardButton(text='🍕 Меню')
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите действие ниже',
    selective=True,
)

contacts_btns = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📱 Поделиться номером', request_contact=True),
            KeyboardButton(text='🧭 Отправить где я', request_location=True)
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Поделитесь номером телефона для заказа',
    selective=True
)
