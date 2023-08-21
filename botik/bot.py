import sys
import config
import logging
from sql import db_start, create_profile, edit_profile
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ContentType, ParseMode,\
ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.markdown import text, italic, code


logging.basicConfig(level=logging.INFO)

Token = config.token
bot = Bot(token=Token)
dp = Dispatcher(bot)

HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>начало работы</em>
<b>/price_list</b> - <em>прайс лист</em>"""

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton('/помощь'))
async def on_startup(_):
    logging.info("Bot started")

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(f"✋🏻✋🏼✋🏽✋🏾✋🏿Приветсвую, {message.chat.first_name}!", 
                        reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['help', 'помощь'])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, 
                            text=HELP_COMMAND, 
                            parse_mode="HTML",
                            reply_markup=ReplyKeyboardRemove())
    await message.delete()

@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(message: types.Message):
    message_text = text(('Я не знаю, что с этим делать 🥶'),
                        italic('\nЯ просто напомню,'), 'что есть',
                        code('команда'), '/help') 
    await message.reply(message_text, parse_mode=ParseMode.MARKDOWN)
    await message.delete()

try:
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
except Exception as e:
    logging.error(f"Error occurred while polling: {e}")