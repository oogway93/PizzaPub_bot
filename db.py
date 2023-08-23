import sqlite3 as sq

from pizza_data import images, names, descriptions, prices
from keyboards import keyboards
import main

base = sq.connect('pizza_hp.db')
cur = base.cursor()


def sql_start_db():
    if base:
        print("DB was started(created)")

    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()

    all_data = base.execute('SELECT * FROM menu')
    if len(all_data.fetchall()) == 0:
        for i in range(5):
            cur.execute(f'INSERT INTO menu VALUES ("{images[i]}", "{names[i]}", "{descriptions[i]}", "{prices[i]}")')
            base.commit()
            print(f"Data_{i + 1} in db")

# Do this code in a python console
# from pizza_data import images, names, descriptions, prices
# for i in range(5):
#     cur.execute(f'INSERT INTO menu VALUES ("{images[i]}", "{names[i]}", "{descriptions[i]}", "{prices[i]}")')
#     base.commit()
#     print("Data in db")


async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await main.bot.send_photo(message.from_user.id, ret[0],
                                  f'<b><u>{ret[1]}</u></b>\n\nОписание: {ret[2]}\nЦена: <em>{ret[-1]}</em> руб',
                                  parse_mode='HTML', reply_markup=keyboards.ikb)
