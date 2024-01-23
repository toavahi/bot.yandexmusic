import logging

import asyncio
from aiogram import Bot, Router, Dispatcher, types, html
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode
from aiogram.fsm.state import State, StatesGroup
from run import *

API_TOKEN = '6596069965:AAFRNeaCnD_vm9Psuz4vVEB2Vuou3xg2M1Y'

logging.basicConfig(level=logging.INFO)
dp = Dispatcher()
form_router = Router()


class Form(StatesGroup):
    search = State()
    result = State()


@dp.message(commands=['start'])
async def start(message: types.Message) -> None:
    await message.reply("ДАРОВА ЭУ")


async def main():
    bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include.router(form_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
