from aiogram.utils.keyboard import InlineKeyboardBuilder

from botik.data.db_callback_managment import DbCallbackFactory

def admin_panel():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Добавить запись",
        callback_data=DbCallbackFactory(action="add")
    )
    builder.button(
        text="Удалить запись",
        callback_data=DbCallbackFactory(action="delete")
    )
    builder.button(
        text="Изменить запись",
        callback_data=DbCallbackFactory(action="edit")
    )
    builder.button(
        text="Показать базу данных",
        callback_data=DbCallbackFactory(action="show")
    )
    builder.adjust(4)
    return builder.as_markup()

def vape_or_liquid():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Одноразки",
        callback_data=DbCallbackFactory(action="vape", type="vape")
    )
    builder.button(
        text="Жижи",
        callback_data=DbCallbackFactory(action="liquid", type="liquid")
    )
    builder.button(
        text="Назад",
        callback_data=DbCallbackFactory(action="back")
    )
    builder.adjust(3)
    return builder.as_markup()