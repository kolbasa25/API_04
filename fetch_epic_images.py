import argparse
import os
from datetime import datetime

import requests

from image_tools import download_image


EPIC_ALL_DATES_URL = "https://epic.gsfc.nasa.gov/api/natural/all"
EPIC_DATE_URL_TEMPLATE = "https://epic.gsfc.nasa.gov/api/natural/date/{date}"
EPIC_IMAGE_URL_TEMPLATE = "https://epic.gsfc.nasa.gov/archive/natural/{year}/{month}/{day}/png/{image}.png"


def get_latest_date():
    response = requests.get(EPIC_ALL_DATES_URL, timeout=20)
    response.raise_for_status()
    dates = response.json()

    if not dates:
        return None

    return max(item["date"] for item in dates)


def get_epic_image_url(item):
    image_date = datetime.strptime(item["date"], "%Y-%m-%d %H:%M:%S")
    return EPIC_IMAGE_URL_TEMPLATE.format(
        year=image_date.strftime("%Y"),
        month=image_date.strftime("%m"),
        day=image_date.strftime("%d"),
        image=item["image"],
    )


def fetch_epic_images(count):
    if not 1 <= count <= 10:
        raise ValueError("count должен быть от 1 до 10")

    os.makedirs("images", exist_ok=True)

    date = get_latest_date()
    if not date:
        print("NASA EPIC не вернул даты")
        return

    response = requests.get(EPIC_DATE_URL_TEMPLATE.format(date=date), timeout=20)
    response.raise_for_status()
    items = response.json()

    for index, item in enumerate(items[:count], start=1):
        image_url = get_epic_image_url(item)
        file_path = os.path.join("images", f"epic_{index}.png")

        try:
            download_image(image_url, file_path)
            print(f"Сохранено: {file_path}")
        except requests.exceptions.RequestException:
            print(f"Не удалось скачать {image_url}")


def main():
    parser = argparse.ArgumentParser(
        description="Скачивает последние EPIC-изображения Земли с сайта NASA"
    )
    parser.add_argument(
        "--count",
        type=int,
        default=5,
        choices=range(1, 11),
        metavar="1-10",
        help="Количество изображений (от 1 до 10, по умолчанию 5)",
    )
    args = parser.parse_args()

    fetch_epic_images(args.count)


if __name__ == "__main__":
    main()