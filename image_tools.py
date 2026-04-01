import os
from urllib.parse import urlparse
from os.path import splitext

import requests


def create_folder(folder_name):
    os.makedirs(folder_name, exist_ok=True)


def get_file_extension(url):
    path = urlparse(url).path
    extension = splitext(path)[1]
    return extension or ".jpg"


def download_image(url, file_path, proxies=None):
    response = requests.get(url.strip(), proxies=proxies, timeout=30)
    response.raise_for_status()

    with open(file_path, "wb") as file:
        file.write(response.content)