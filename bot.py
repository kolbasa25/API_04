import os
from dotenv import load_dotenv
from telegram import Bot


load_dotenv()

bot = Bot(token=os.environ["TELEGRAM_TOKEN"])
chat_id = os.environ["TELEGRAM_CHAT_ID"]

with open("images/spacex_1.jpg", "rb") as photo:
    bot.send_photo(chat_id=chat_id, photo=photo)