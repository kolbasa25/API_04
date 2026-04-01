import os
import time
import random
import argparse

from dotenv import load_dotenv
from telegram import Bot


def get_image_files(folder_name):
    image_files = []

    for filename in os.listdir(folder_name):
        file_path = os.path.join(folder_name, filename)

        if os.path.isfile(file_path):
            image_files.append(file_path)

    return image_files


def publish_image(bot, chat_id, image_path):
    with open(image_path, "rb") as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)

    print(f"Опубликовано: {image_path}")


def publish_images(folder_name, delay_hours, bot, chat_id):
    image_files = get_image_files(folder_name)

    if not image_files:
        print("В папке нет файлов для публикации")
        return

    delay_seconds = delay_hours * 3600

    while True:
        random.shuffle(image_files)

        for image_path in image_files:
            publish_image(bot, chat_id, image_path)
            time.sleep(delay_seconds)


def main():
    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument("folder_name", nargs="?", default="images")
    parser.add_argument("--hours", type=float, default=None)
    args = parser.parse_args()

    telegram_token = os.environ["TELEGRAM_TOKEN"]
    telegram_chat_id = os.environ["TELEGRAM_CHAT_ID"]

    delay_hours = args.hours
    if delay_hours is None:
        delay_hours = float(os.environ.get("PUBLISH_DELAY_HOURS", 4))

    bot = Bot(token=telegram_token)
    publish_images(args.folder_name, delay_hours, bot, telegram_chat_id)


if __name__ == "__main__":
    main()