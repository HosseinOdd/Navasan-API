# Navasan Data Scraper

A lightweight Python tool for fetching the latest **currency** and **gold** rates from [Navasan.net](https://www.navasan.net).

The project uses **Selenium** and **HTTP requests** to retrieve data and keeps it updated automatically via **GitHub Actions**, with a daily price history archived alongside it.

---

## Automated Updates

Data is refreshed **every 30 minutes** using GitHub Actions, without requiring any paid service.

**Live JSON data:**
- Fiat currencies: [`data/fiat.json`](./data/fiat.json)
- Gold and coin rates: [`data/gold.json`](./data/gold.json)

**Raw URLs for direct consumption:**

```
https://raw.githubusercontent.com/HosseinOdd/Navasan-API/main/data/fiat.json
https://raw.githubusercontent.com/HosseinOdd/Navasan-API/main/data/gold.json
```

---

## Features

- Headless Chrome automation with Selenium
- Session handling via `PHPSESSID`
- Dynamic CSRF token generation
- Fetches:
  - Fiat currency rates
  - Gold and coin prices
- Stores results as structured JSON
- Daily price history, dated in Tehran time (UTC+03:30)
- Fully automated updates via GitHub Actions
- Automatic GitHub releases on version tags

---

## Project Structure

```
.
├── .github/
│   ├── release.yml
│   └── workflows/
│       ├── update-data.yml
│       └── release.yml
├── data/
│   ├── fiat.json
│   ├── gold.json
│   └── history/
│       ├── 2026-11-07.json
│       └── 2026-11-08.json
├── src/
│   └── app.py
├── requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/HosseinOdd/Navasan-API.git
cd Navasan-API
```

---

## Requirements

- Python 3.8+
- Google Chrome

ChromeDriver does not need to be installed manually. Selenium 4.6+ ships with Selenium Manager, which downloads a driver matching your installed Chrome.

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the script:

```bash
python src/app.py
```

The script will:
- Start a headless browser session
- Generate the required authentication tokens
- Fetch the latest data and store it in the `data/` directory
- Write the current day's snapshot to `data/history/`

---

## Output

- `data/fiat.json`: Fiat currency exchange rates
- `data/gold.json`: Gold and coin prices (Iran market)
- `data/history/YYYY-MM-DD.json`: Daily snapshot of both datasets

### History

One file is kept per day, named after the date in Tehran time. The file is overwritten on every run, so it always contains the latest prices of that day. Each file has the following shape:

```json
{
  "date": "2026-11-08",
  "timestamp": "2026-11-08T14:30:00+03:30",
  "fiat": { },
  "gold": { }
}
```

If one of the two requests fails during a run, the previously stored value for that day is preserved instead of being replaced with `null`.

Intraday changes are also available through the Git commit history of each file.

---

## Disclaimer

**Made with ❤️ for automation and data collection**
Please review and respect the terms of service of the data source.
