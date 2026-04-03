import os
import argparse

from dotenv import load_dotenv
from telegram import Bot

from image_tools import send_telegram_image


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="Отправляет одно изображение в Telegram-канал"
    )
    parser.add_argument(
        "image_path",
        help="Путь к изображению",
    )
    args = parser.parse_args()

    telegram_token = os.environ["TELEGRAM_TOKEN"]
    telegram_chat_id = os.environ["TELEGRAM_CHAT_ID"]

    bot = Bot(token=telegram_token)
    send_telegram_image(bot, telegram_chat_id, args.image_path)
    print(f"Отправлено: {args.image_path}")


if __name__ == "__main__":
    main()