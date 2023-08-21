from aiogram import Bot, Router, F
from aiogram.filters import Command
from aiogram.types import Message

from botik.filters.is_admin import IsAdminFilter
from botik.settings import settings 
from botik.keyboards.basic_keyboard import katalog_help_kb

router = Router()

@router.message(Command("start"))
async def get_start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}, рады вас видеть!",
                         reply_markup=katalog_help_kb())

@router.message(F.text=="Помощь")
async def help_command(message: Message):
    await message.answer("Хм")