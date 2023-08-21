from aiogram import Bot, Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from botik.db.show_db_table import show_vape, show_vape_liquid

from botik.keyboards.admin_panel import admin_panel, vape_or_liquid

from botik.filters.is_admin import IsAdminFilter

from botik.data.db_callback_managment import DbCallbackFactory

router = Router()

@router.callback_query(DbCallbackFactory.filter(F.action == "add"))
async def callback_db_add(
    callback: CallbackQuery
):
    await callback.message.edit_text(text="Выберите тип товара", reply_markup=vape_or_liquid())
    await callback.answer()

@router.callback_query(DbCallbackFactory.filter(F.action == "delete"))
async def callback_db_delete(
    callback: CallbackQuery
):
    await callback.message.edit_text(text="Выберите тип товара", reply_markup=vape_or_liquid())
    await callback.answer()

@router.callback_query(DbCallbackFactory.filter(F.action == "edit"))
async def callback_db_edit(
    callback: CallbackQuery
):
    await callback.message.edit_text(text="Выберите тип товара", reply_markup=vape_or_liquid())
    await callback.answer()

@router.callback_query(DbCallbackFactory.filter(F.action == "show"))
async def callback_db_show(
    callback: CallbackQuery
):
    await callback.message.edit_text(text="Выберите тип товара", reply_markup=vape_or_liquid())
    await callback.answer()

@router.callback_query(DbCallbackFactory.filter(F.action == "vape" and F.type == "vape"))
async def show_vape_table(
    callback: CallbackQuery
):
    vape_table = await show_vape()
    await callback.message.answer(text=f"{vape_table}")
    await callback.answer()

@router.callback_query(DbCallbackFactory.filter(F.action == "liquid" and F.type == "liquid"))
async def show_liquid_table(
    callback: CallbackQuery
):
    vape_liquid_table = await show_vape_liquid()
    await callback.message.answer(text=f"{vape_liquid_table}")
    await callback.answer()

@router.callback_query(DbCallbackFactory.filter(F.action == "back"))
async def back_button(
    callback: CallbackQuery
):
    await callback.message.edit_text("You are an admin!", reply_markup=admin_panel())
    await callback.answer()

@router.message(IsAdminFilter(is_admin=True), Command("admin"))
async def start_admin(message: Message, bot: Bot):
    await bot.send_message(chat_id=message.chat.id ,text="You are an admin!", reply_markup=admin_panel())