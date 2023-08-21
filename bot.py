import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

from botik.handlers import basic, admin_route

from botik.settings import settings

from botik.utils.command_menu import set_commands

async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text="Bot is on!")

async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="Bot is off!")
    
async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                        "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s ")
    
    bot = Bot(token=settings.bots.bot_token)

    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.include_routers(basic.router, admin_route.router)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())