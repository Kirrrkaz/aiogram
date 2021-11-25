from aiogram import Bot, Dispatcher, executor, types
import logging

API_TOKEN = '2043446098:AAHrPgihpoE3TCLM_WTZQKb5YwDzfEYyqoY'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    p = open("bird.jpg", "rb")
    await bot.send_photo(message.chat.id, p)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True) 
