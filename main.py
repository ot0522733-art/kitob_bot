import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Bot tokeningizni shu yerga yozing
API_TOKEN = '8823316737:AAG8OxaHDgW-MlELlkSA2qtUxy7Jym7K15E'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Salom! Botimiz ishlayapti.")

if name == 'main':
    executor.start_polling(dp, skip_updates=True)
