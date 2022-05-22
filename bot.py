from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN
from constsnts import MainMenu, Table, Lib, BACK_BUTTON
from entry_status import date_entry
from lib.lib import get_lib, get_category_lib
from table.table import choose_day, get_tomorrow, get_today, get_week, get_for_date, set_entry_date

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    button_table = KeyboardButton(MainMenu.TABLE)
    button_campus = KeyboardButton(MainMenu.CAMPUS)
    button_lib = KeyboardButton(MainMenu.LIB)

    key = ReplyKeyboardMarkup(resize_keyboard=True)
    key.add(button_table, button_campus).add(button_lib)
    await message.reply("Выберите, что Вы хотите просмотреть:", reply_markup=key)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("что за бот, описание")


@dp.message_handler()
async def ans_message(msg: types.Message):
    ans = msg.text
    if msg.text == MainMenu.TABLE:
        await choose_day(msg)
    elif msg.text == MainMenu.CAMPUS:
        await bot.send_message(msg.from_user.id, ans)
    elif msg.text == MainMenu.LIB:
        await get_lib(msg)

    elif msg.text == BACK_BUTTON:
        await process_start_command(msg)

    elif msg.text == Table.TODAY:
        await get_today(msg)
    elif msg.text == Table.TOMORROW:
        await get_tomorrow(msg)
    elif msg.text == Table.WEEK:
        await get_week(msg)
    elif msg.text == Table.DATE:
        await set_entry_date(msg)

    elif (msg.text == Lib.URB or
          msg.text == Lib.PUB or
          msg.text == Lib.PER or
          msg.text == Lib.PHIL or
          msg.text == Lib.PHOTO or
          msg.text == Lib.CUR or
          msg.text == Lib.DIS or
          msg.text == Lib.ARH or
          msg.text == Lib.ISK or
          msg.text == Lib.CHILD or
          msg.text == Lib.SOC or
          msg.text == Lib.ALB):
        await get_category_lib(msg)


    else:
        if date_entry.get_status():
            await get_for_date(msg)
        else:
            await msg.reply("Для получения справки введите команду /help")


if __name__ == '__main__':
    executor.start_polling(dp)
