from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = KeyboardButton('/Schedule')
btn2 = KeyboardButton('/Location')
btn3 = KeyboardButton('/Menu')
btn4 = KeyboardButton('Поделиться номером', request_contact=True)
btn5 = KeyboardButton('Отправить где я', request_location=True)
kb.add(btn3).add(btn1, btn2).add(btn4, btn5)

ikb = InlineKeyboardMarkup()
ibtn1 = InlineKeyboardButton("❤️", callback_data="Like")
ibtn2 = InlineKeyboardButton("👎", callback_data="Dislike")
ikb.add(ibtn1, ibtn2)
