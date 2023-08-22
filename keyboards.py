from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Command

kb = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = KeyboardButton('/Schedule')
btn2 = KeyboardButton('/Location')
btn3 = KeyboardButton('/Menu')
btn4 = KeyboardButton('Поделиться номером', request_contact=True)
btn5 = KeyboardButton('Отправить где я', request_location=True)
kb.add(btn3).add(btn1, btn2).add(btn4, btn5)

# ikb = InlineKeyboardMarkup()
# ibtn1 = InlineKeyboardButton("Пеперонни",
#                              url="https://dodopizza-a.akamaihd.net/static/Img/Products/27c9bbd0af3a4d1d84a086d9c2f1656d_292x292.webp",
#                              callback_data="")
# ibtn2 = InlineKeyboardButton("Двойной Цыпленок",
#                              url="https://dodopizza-a.akamaihd.net/static/Img/Products/cea570842b754c52b786c231c65bd2e2_292x292.webp")
# ibtn3 = InlineKeyboardButton("Песто",
#                              url="https://dodopizza-a.akamaihd.net/static/Img/Products/6046174c06e440299c4e7117a8ecfea4_292x292.webp")
# ikb.add(ibtn1, ibtn2).add(ibtn3)



