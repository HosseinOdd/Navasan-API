import os
import time
import json
import base64
import requests
from datetime import datetime, timezone, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
HISTORY_DIR = os.path.join(DATA_DIR, 'history')
FIAT_PATH = os.path.join(DATA_DIR, 'fiat.json')
GOLD_PATH = os.path.join(DATA_DIR, 'gold.json')

TEHRAN_TZ = timezone(timedelta(hours=3, minutes=30))


def get_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(options=options)


def get_phpsessid(driver, url):
    driver.get(url)
    WebDriverWait(driver, 10).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )
    time.sleep(2)
    for cookie in driver.get_cookies():
        if cookie['name'] == 'PHPSESSID':
            return cookie['value']
    return None


def make_request(driver, endpoint, filename, csrf_token):
    unix_time = int(time.time())
    url = f"https://www.navasan.net/{endpoint}?csrf={csrf_token}&_={unix_time}"

    cookies = {c['name']: c['value'] for c in driver.get_cookies()}
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://www.navasan.net/',
    }

    try:
        response = requests.get(url, headers=headers, cookies=cookies, timeout=15)
        response.raise_for_status()
        data = response.json()
    except (requests.RequestException, ValueError):
        return None

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return data


def save_history(fiat_data, gold_data):
    if fiat_data is None and gold_data is None:
        return

    os.makedirs(HISTORY_DIR, exist_ok=True)

    now = datetime.now(TEHRAN_TZ)
    date_str = now.strftime('%Y-%m-%d')
    history_path = os.path.join(HISTORY_DIR, f"{date_str}.json")

    record = {
        "date": date_str,
        "timestamp": now.isoformat(),
        "fiat": fiat_data,
        "gold": gold_data,
    }

    if os.path.exists(history_path):
        try:
            with open(history_path, 'r', encoding='utf-8') as f:
                previous = json.load(f)
            record["fiat"] = record["fiat"] or previous.get("fiat")
            record["gold"] = record["gold"] or previous.get("gold")
        except (ValueError, OSError):
            pass

    with open(history_path, 'w', encoding='utf-8') as f:
        json.dump(record, f, indent=2, ensure_ascii=False)


def main():
    url = "https://www.navasan.net/"
    prefix = "2bba8a6abdcae9571d63fefcd1df29bb3a8f5d91http://www.navasan.net/54tf%f"

    os.makedirs(DATA_DIR, exist_ok=True)

    driver = get_driver()
    try:
        phpsessid = get_phpsessid(driver, url)
        if not phpsessid:
            return
        csrf_token = base64.b64encode((prefix + phpsessid).encode()).decode()

        fiat_data = make_request(driver, "last_currencies.php", FIAT_PATH, csrf_token)
        gold_data = make_request(driver, "gold_rates.php", GOLD_PATH, csrf_token)

        save_history(fiat_data, gold_data)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()