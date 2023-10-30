from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_btns = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='❤️', callback_data='Like'),
            InlineKeyboardButton(text='👎', callback_data='Dislike'),
        ]
    ]
)
