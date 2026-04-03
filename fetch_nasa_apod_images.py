import argparse
import os

import requests
from dotenv import load_dotenv

from image_tools import download_image, get_file_extension


NASA_APOD_URL = "https://api.nasa.gov/planetary/apod"


def fetch_nasa_apod_images(api_key, count):
    if not 1 <= count <= 100:
        raise ValueError("count должен быть от 1 до 100")

    os.makedirs("images", exist_ok=True)

    params = {
        "api_key": api_key,
        "count": count,
    }

    response = requests.get(NASA_APOD_URL, params=params, timeout=20)
    response.raise_for_status()
    items = response.json()

    image_items = [
        item for item in items
        if item.get("media_type") == "image"
    ]

    for image_number, item in enumerate(image_items, start=1):
        image_url = (item.get("hdurl") or item.get("url") or "").strip()
        if not image_url:
            continue

        extension = get_file_extension(image_url)
        file_path = os.path.join("images", f"nasa_apod_{image_number}{extension}")

        try:
            download_image(image_url, file_path)
            print(f"Сохранено: {file_path}")
        except requests.exceptions.RequestException:
            print(f"Не удалось скачать {image_url}")


def main():
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="Скачивает случайные изображения NASA APOD"
    )
    parser.add_argument(
        "--count",
        type=int,
        default=30,
        choices=range(1, 101),
        metavar="1-100",
        help="Количество изображений (от 1 до 100, по умолчанию 30)",
    )
    args = parser.parse_args()

    api_key = os.environ.get("NASA_API_KEY")
    if api_key is None:
        raise ValueError("Не найден NASA_API_KEY в .env")

    fetch_nasa_apod_images(api_key, args.count)


if __name__ == "__main__":
    main()