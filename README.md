# Космический Телеграм

Проект автоматически скачивает космические изображения из API NASA и SpaceX и публикует их в Telegram-канал.

---

## Установка

Требуется установленный Python 3.

Установите зависимости:

```bash
pip install -r requirements.txt
```

Создайте файл `.env` и добавьте:

```bash
NASA_API_KEY=ваш_nasa_api_key
TELEGRAM_TOKEN=ваш_telegram_token
TELEGRAM_CHAT_ID=@your_channel_name
PUBLISH_DELAY_HOURS=4
```

Ключи и API берутся здесь:
- NASA API: https://api.nasa.gov/
- NASA EPIC: https://epic.gsfc.nasa.gov/
- SpaceX API: https://github.com/r-spacex/SpaceX-API
- Telegram-бот: создаётся через @BotFather
- `TELEGRAM_CHAT_ID` для канала указывается в формате `@your_channel_name`

---

## Скрипты

### fetch_nasa_apod_images.py

Скачивает случайные изображения NASA APOD.

```bash
python fetch_nasa_apod_images.py
```

По умолчанию скрипт скачивает 30 изображений. Если нужно изменить количество, используйте параметр `--count`. Допустимое количество изображений: от 1 до 100.

```bash
python fetch_nasa_apod_images.py --count 10
```

Для работы нужен `NASA_API_KEY` в файле `.env`.

---

### fetch_spacex_images.py

Скачивает фотографии последнего запуска SpaceX.

```bash
python fetch_spacex_images.py
```

Если нужно скачать изображения конкретного запуска, укажите `launch_id`:

```bash
python fetch_spacex_images.py 5eb87d47ffd86e000604b38a
```

Если нужен прокси, используйте параметр `--proxy`:

```bash
python fetch_spacex_images.py --proxy socks5://95.179.255.75:1080
```

---

### fetch_epic_images.py

Скачивает последние доступные EPIC-изображения Земли.

```bash
python fetch_epic_images.py
```

По умолчанию скрипт скачивает 5 изображений. Если нужно изменить количество, используйте параметр `--count`. Допустимое количество изображений: от 1 до 10.

```bash
python fetch_epic_images.py --count 3
```

---

### publish_images.py

Публикует изображения из папки в Telegram-канал по кругу с заданным интервалом.

```bash
python publish_images.py
```

По умолчанию берётся папка `images`, а интервал публикации — из переменной `PUBLISH_DELAY_HOURS` в файле `.env`.

Если нужно изменить интервал, используйте `--hours`:

```bash
python publish_images.py --hours 2
```

Если нужно указать другую папку:

```bash
python publish_images.py my_images --hours 2
```

---

### send_image.py

Публикует одно изображение в Telegram-канал.

```bash
python send_image.py images/spacex_1.jpg
```

---

### image_tools.py

Вспомогательный модуль для:
- создания папок
- определения расширения файла по ссылке
- скачивания изображений по URL

---

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.