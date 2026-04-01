import argparse
import os

import requests

from image_tools import create_folder, download_image


SPACEX_URL = "https://api.spacexdata.com/v5/launches"


def fetch_spacex_images(launch_id=None, proxy=None):
    create_folder("images")

    proxies = None
    if proxy:
        proxies = {
            "http": proxy,
            "https": proxy,
        }

    if launch_id:
        url = f"{SPACEX_URL}/{launch_id}"
        response = requests.get(url, proxies=proxies, timeout=20)
        response.raise_for_status()
        launch = response.json()
        images = launch.get("links", {}).get("flickr", {}).get("original", [])
    else:
        response = requests.get(SPACEX_URL, proxies=proxies, timeout=20)
        response.raise_for_status()
        launches = response.json()

        images = []
        for launch in reversed(launches):
            images = launch.get("links", {}).get("flickr", {}).get("original", [])
            if images:
                break

    for index, image_url in enumerate(images, start=1):
        file_path = os.path.join("images", f"spacex_{index}.jpg")
        download_image(image_url, file_path)
        print(f"Сохранено: {file_path}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("launch_id", nargs="?", default=None)
    parser.add_argument("--proxy", default=None)
    args = parser.parse_args()

    fetch_spacex_images(args.launch_id, args.proxy)


if __name__ == "__main__":
    main()