from urllib.parse import urlparse
from os.path import splitext

import requests


def get_file_extension(url):
    path = urlparse(url).path
    extension = splitext(path)[1]
    return extension or ".jpg"


def download_image(url, file_path, proxies=None):
    response = requests.get(url.strip(), proxies=proxies, timeout=30)
    response.raise_for_status()

    with open(file_path, "wb") as file:
        file.write(response.content)


def send_telegram_image(bot, chat_id, image_path):
    with open(image_path, "rb") as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)