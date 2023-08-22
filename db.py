import sqlite3 as sq

import keyboards
from main import bot

''' создаём базу данных (если уже есть - подключаемся к ней)'''

base = sq.connect('pizza_hp.db')
cur = base.cursor()
if base:
    print('Data base connected OK!')
base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
base.commit()


# async def sql_add_command(state):
#     async with state.proxy() as data:
#         cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
#         base.commit()


async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0],
                             f'<b><u>{ret[1]}</u></b>\n\nОписание: {ret[2]}\nЦена: <em>{ret[-1]}</em> руб',
                             parse_mode='HTML', reply_markup=keyboards.ikb)

