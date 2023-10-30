from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_btns = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Schedule'),
            KeyboardButton(text='Location'),
        ],
        [
            KeyboardButton(text='Menu')
        ],
        [
            KeyboardButton(text='Поделиться номером', request_contact=True),
            KeyboardButton(text='Отправить где я', request_location=True)
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите действие ниже',
    selective=True,
)
