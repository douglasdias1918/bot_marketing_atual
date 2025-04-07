from aiogram import Bot, Dispatcher, executor, types
import logging
import asyncio

API_TOKEN = 'SEU_TOKEN_AQUI'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Bem-vindo ao Bot de Marketing Inteligente!")

def start_bot():
    executor.start_polling(dp, skip_updates=True)
