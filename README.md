# Navasan Data Scraper

A lightweight Python tool for fetching the latest **currency** and **gold** rates from [Navasan.net](https://www.navasan.net).

The project uses **Selenium** and **HTTP requests** to securely retrieve data and keeps it automatically updated via **GitHub Actions**.

---

## Automated Updates

Data is refreshed **every 10 minutes** using GitHub Actions, without requiring any paid service.

**Live JSON data:**
- Fiat currencies: [`data/fiat.json`](./data/fiat.json)
- Gold and coin rates: [`data/gold.json`](./data/gold.json)

---

## Features

- Headless Chrome automation with Selenium  
- Secure session handling via `PHPSESSID`
- Dynamic CSRF token generation
- Fetches:
  - Fiat currency rates
  - Gold and coin prices
- Stores results as structured JSON
- Fully automated updates via GitHub Actions

---

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── update-data.yml
├── data/
│   ├── fiat.json
│   └── gold.json
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

- Python 3.7+
- Google Chrome
- ChromeDriver (compatible with installed Chrome)

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
- Generate required authentication tokens
- Fetch and store the latest data in the `data/` directory

---

## Output

- `fiat.json`: Fiat currency exchange rates  
- `gold.json`: Gold and coin prices (Iran market)

---

## Disclaimer

**Made with ❤️ for automation and data collection**
Please review and respect the terms of service of the data source.
