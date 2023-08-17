import logging
from aiogram import Bot, Dispatcher, executor, types
from decouple import config
import random

bot = Bot(config("API_TOKEN"))
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.message):
    await message.answer("Hello, i am telegram bot")
    
@dp.message_handler()
async def echo(message: types.message):
    await message.answer(message.text)
    
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)