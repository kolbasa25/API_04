import os
from dotenv import load_dotenv
from telegram import Bot


load_dotenv()

bot = Bot(token=os.environ["TELEGRAM_TOKEN"])

chat_id = os.environ["TELEGRAM_CHAT_ID"]

bot.send_message(chat_id=chat_id, text="Привет")