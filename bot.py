import asyncio
import logging
import sys
from os import getenv
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from run import *
from aiogram.filters import Command


TOKEN = '6669241077:AAEF9-l44cZOsp7AKx3GsK8tczLM-KsZhaw'


dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message(Command("like"))
async def like(message: types.message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="like a track",
        callback_data="random_value")
    )

    await message.answer(
        "done"
    )

@dp.message(Command("dislike"))
async def dislike(message: types.message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="dislike a track",
        callback_data="random_value")
    )

    await message.answer(
        "done1"
    )


@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:
        temp = search(message.text)
        await message.answer(temp['title'] + '-' + temp['artists'][0]['name'])
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


