import os
import time
import random
import argparse

from dotenv import load_dotenv
from telegram import Bot

from image_tools import send_telegram_image


def get_image_files(folder_name):
    image_files = []

    for filename in os.listdir(folder_name):
        file_path = os.path.join(folder_name, filename)

        if os.path.isfile(file_path):
            image_files.append(file_path)

    return image_files


def publish_images(image_files, delay_hours, bot, chat_id):
    if not image_files:
        print("В папке нет файлов для публикации")
        return

    delay_seconds = delay_hours * 3600

    while True:
        random.shuffle(image_files)

        for image_path in image_files:
            send_telegram_image(bot, chat_id, image_path)
            print(f"Опубликовано: {image_path}")
            time.sleep(delay_seconds)


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="Публикует изображения в Telegram-канал с заданным интервалом"
    )
    parser.add_argument(
        "folder_name",
        nargs="?",
        default="images",
        help="Папка с изображениями (по умолчанию: images)",
    )
    parser.add_argument(
        "--hours",
        type=float,
        metavar="HOURS",
        help="Интервал публикации в часах (по умолчанию берётся из .env)",
    )
    args = parser.parse_args()

    telegram_token = os.environ["TELEGRAM_TOKEN"]
    telegram_chat_id = os.environ["TELEGRAM_CHAT_ID"]

    delay_hours = args.hours
    if delay_hours is None:
        delay_hours = float(os.environ.get("PUBLISH_DELAY_HOURS", 4))

    bot = Bot(token=telegram_token)
    image_files = get_image_files(args.folder_name)
    publish_images(image_files, delay_hours, bot, telegram_chat_id)


if __name__ == "__main__":
    main()