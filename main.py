from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from random import randint
import json

token = "5242322897:AAEUhdgrDyDKrsuZd7C42w9yvqI6o_sJX-g"

bot = Bot(token=token)

dp = Dispatcher(bot)

compliment_button = KeyboardButton("/compliment")
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(compliment_button)


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.reply("Hello world", reply_markup=keyboard)


@dp.message_handler(commands=["compliment"])
async def start_handler(message: types.Message):
    with open("compliments.json", 'rb') as my_json:
        compliments_json = json.loads(my_json.read())
    compliment_id = randint(0, len(compliments_json["data"]) - 1)
    await message.reply(compliments_json["data"][compliment_id]["title"], reply_markup=keyboard)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
