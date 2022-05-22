from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from constsnts import Lib, LibLink, BACK_BUTTON
from lib.get_data import get_books


async def get_lib(message: types.Message):
    button_1 = KeyboardButton(Lib.ALB)
    button_2 = KeyboardButton(Lib.CHILD)
    button_3 = KeyboardButton(Lib.ISK)
    button_4 = KeyboardButton(Lib.PER)
    button_5 = KeyboardButton(Lib.SOC)
    button_6 = KeyboardButton(Lib.PHIL)
    button_7 = KeyboardButton(Lib.ARH)
    button_8 = KeyboardButton(Lib.DIS)
    button_9 = KeyboardButton(Lib.CUR)
    button_10 = KeyboardButton(Lib.PUB)
    button_11 = KeyboardButton(Lib.URB)
    button_12 = KeyboardButton(Lib.PHOTO)

    button_back = KeyboardButton(BACK_BUTTON)

    key = ReplyKeyboardMarkup(resize_keyboard=True)
    key.add(button_1, button_3, button_5, button_7, button_9, button_11) \
        .add(button_2, button_4, button_6, button_8, button_10, button_12) \
        .add(button_back)
    await message.reply("Выберите раздел", reply_markup=key)


async def get_category_lib(message: types.Message):
    link = ""
    books = []
    if message.text == Lib.URB:
        link = LibLink.URB
        books = get_books(Lib.URB, "lib")
    elif message.text == Lib.ALB:
        link = LibLink.ALB
        books = get_books(Lib.ALB, "lib")
    elif message.text == Lib.CHILD:
        link = LibLink.CHILD
        books = get_books(Lib.CHILD, "lib")
    elif message.text == Lib.ISK:
        link = LibLink.ISK
        books = get_books(Lib.ISK, "lib")
    elif message.text == Lib.PER:
        link = LibLink.PER
        books = get_books(Lib.PER, "lib")
    elif message.text == Lib.SOC:
        link = LibLink.SOC
        books = get_books(Lib.SOC, "lib")
    elif message.text == Lib.PHIL:
        link = LibLink.PHIL
        books = get_books(Lib.PHIL, "lib")
    elif message.text == Lib.ARH:
        link = LibLink.ARH
        books = get_books(Lib.ARH, "lib")
    elif message.text == Lib.DIS:
        link = LibLink.DIS
        books = get_books(Lib.DIS, "lib")
    elif message.text == Lib.CUR:
        link = LibLink.CUR
        books = get_books(Lib.CUR, "lib")
    elif message.text == Lib.PUB:
        link = LibLink.PUB
        books = get_books(Lib.PUB, "lib")
    elif message.text == Lib.PHOTO:
        link = LibLink.PHOTO
        books = get_books(Lib.PHOTO, "lib")

    book_ans = ""
    for book in books:
        book_ans += "📖" + book[0] + "\n" + \
                    "Ссылка на книгу: " + book[1] + "\n\n"

    ans = "В библиотеке вы сможете найти следующие книги из раздела \"" + \
          message.text + "\"\n\n" + \
          book_ans + "\n\n" + \
          "Полный список книнг раздела \"" + message.text + \
          "\" вы можете найти на сайте в соотсвующем разделе " + \
          link

    await message.reply(ans)
