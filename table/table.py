from datetime import date, datetime, timedelta

from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from constsnts import Category, CategoryLink, Table, BACK_BUTTON
from entry_status import date_entry
from table.get_data import get_table


async def choose_day(message: types.Message):
    button_today = KeyboardButton(Table.TODAY)
    button_tomorrow = KeyboardButton(Table.TOMORROW)
    button_week = KeyboardButton(Table.WEEK)
    button_date = KeyboardButton(Table.DATE)
    button_back = KeyboardButton(BACK_BUTTON)

    key = ReplyKeyboardMarkup(resize_keyboard=True)
    key.add(button_today, button_tomorrow).add(button_week, button_date).add(button_back)
    await message.reply("Выберите, что Вы хотите посмотреть", reply_markup=key)


async def get_today(message: types.Message):
    today = str(date.today())
    day, month = today.split('-')[2], today.split('-')[1]
    need_date = day + "." + month

    table = get_table(need_date, "table")
    table_ans = ""
    for item in table:
        table_ans += "⏰" + item[1] + "\n" + "🤓" + item[0] + "\n\n"

    if table_ans == "":
        ans = "На сегодня никаких событий не запланированно\n\n" + \
              "Вы можете просмотреть все мероприятина на сайте рельсов\n" + \
              CategoryLink.TABLE
    else:
        ans = "Сегодня " + str(today) + " запланированны следующие мероприятия\n\n" + \
              table_ans + "\n" + \
              "Вы можете просмотреть все мероприятина на сайте рельсов\n" + \
              CategoryLink.TABLE

    await message.reply(ans)


def day_week(i):
    return timedelta(days=i)


async def get_tomorrow(message: types.Message):
    tomorrow = str(date.today() + day_week(1))
    day, month = tomorrow.split('-')[2], tomorrow.split('-')[1]
    need_date = day + "." + month

    table = get_table(need_date, "table")
    table_ans = ""
    for item in table:
        table_ans += "⏰" + item[1] + "\n" + "🤓" + item[0] + "\n\n"

    if table_ans == "":
        ans = "На завтра никаких событий не запланированно\n\n" + \
              "Вы можете просмотреть все мероприятина на сайте рельсов\n" + \
              CategoryLink.TABLE
    else:
        ans = "На завтра " + str(tomorrow) + " запланированны следующие мероприятия\n\n" + \
              table_ans + "\n" + \
              "Вы можете просмотреть все мероприятина на сайте рельсов\n" + \
              CategoryLink.TABLE

    await message.reply(ans)


async def get_week(message: types.Message):
    today = date.today()
    week = [today]
    for i in range(1, 7):
        week.append(today + day_week(i))

    table_list = {}
    for date_day in week:
        date_day = str(date_day)
        day, month = date_day.split('-')[2], date_day.split('-')[1]
        need_date = day + "." + month
        table = get_table(need_date, "table")
        table_list[need_date] = table

    table_list_ans = ""
    for date_day in table_list:
        list_title = ""
        for title in table_list[date_day]:
            list_title += "⏰" + title[1] + "\n" "🤓" + title[0] + "\n\n"

        if list_title == "":
            list_title = "На этот день ничего не запланираванно\n"

        table_list_ans += date_day + "\n" + list_title + "\n"

    ans = "На ближайшую неделю запранированны следующие события: \n\n" + \
          table_list_ans + "\n\n" + \
          "Вы можете просмотреть все мероприятина на сайте рельсов\n" + \
          CategoryLink.TABLE

    await message.reply(ans)


async def set_entry_date(message: types.Message):
    status = True
    date_entry.set_status(status)
    await message.reply("Введите день, на который Вы хотите просмотеть расписание в формате \nDD-MM-YYYY")


async def get_for_date(message: types.Message):
    format_date = "%d-%m-%Y"
    try:
        ans_date = str(datetime.strptime(message.text, format_date))
        day, month = ans_date.split('-')[2].split(' ')[0], ans_date.split('-')[1]
        need_date = day + "." + month

        table = get_table(need_date, "table")
        table_ans = ""
        for item in table:
            table_ans += "⏰" + item[1] + "\n" + "🤓" + item[0] + "\n\n"

        if table_ans == "":
            ans = "На " + str(message.text) + " никаких мероприятий не заплонированно\n\n" + \
                  "Вы можете просмотреть все мероприятина на сайте рельсов\n" + \
                  CategoryLink.TABLE

        else:
            ans = "На " + str(message.text) + " запланированны следующие мероприятия\n\n" + \
                  table_ans + "\n" + \
                  "Вы можете просмотреть все мероприятина на сайте рельсов\n" + \
                  CategoryLink.TABLE

        date_entry.set_status(False)

    except ValueError:
        ans = "Вы неправильно ввели дату, попробуйте еще раз или введите команду /start"

    await message.reply(ans)
