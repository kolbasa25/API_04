import os
import argparse

from dotenv import load_dotenv
from telegram import Bot


def send_image(image_path, chat_id, bot):
    with open(image_path, "rb") as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)

    print(f"Отправлено: {image_path}")


def main():
    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument("image_path")
    args = parser.parse_args()

    telegram_token = os.environ["TELEGRAM_TOKEN"]
    telegram_chat_id = os.environ["TELEGRAM_CHAT_ID"]

    bot = Bot(token=telegram_token)
    send_image(args.image_path, telegram_chat_id, bot)


if __name__ == "__main__":
    main()