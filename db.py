import aiosqlite

from aiogram.types import Message

from pizza_data import images, names, descriptions, prices
from keyboards import inline


async def sql_start_db():
    async with aiosqlite.connect('pizza_pub.db') as db:
        if db:
            print("DB was started(created)")
        await db.execute(
            'CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT);'
        )
        await db.commit()
        async with db.execute('SELECT * FROM menu;') as cursor:
            if len(await cursor.fetchall()) == 0:
                for i in range(5):
                    await cursor.execute(
                        f'INSERT INTO menu VALUES ("{images[i]}", "{names[i]}", "{descriptions[i]}", "{prices[i]}")')
                    await db.commit()
                    print(f"Data_{i + 1} in db")


async def sql_read(message: Message):
    async with aiosqlite.connect('pizza_pub.db') as db:
        async with db.execute('SELECT * FROM menu;') as cursor:
            async for ret in cursor:
                await message.answer_photo(ret[0],
                                           f'<b><u>{ret[1]}</u></b>\n\nОписание: {ret[2]}\nЦена: <em>{ret[-1]}</em> руб',
                                           parse_mode='HTML', reply_markup=inline.inline_btns)
