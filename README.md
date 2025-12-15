# 💰 Navasan Data Scraper

A Python script that scrapes the latest **currency** and **gold** rates from [Navasan.net](https://www.navasan.net) using **Selenium** and **Requests**.

## 🤖 Automated Updates

This repository uses **GitHub Actions** to automatically fetch and update currency and gold data **every 5 minutes** for free! The data is always fresh and up-to-date.

📊 **Live Data Access:**
- [Fiat Currency Data (JSON)](./data/fiat.json)
- [Gold Rates Data (JSON)](./data/gold.json)

## 🚀 Features

- Headless Chrome browser using Selenium
- Extracts `PHPSESSID` cookie for secure access
- Generates CSRF token dynamically
- Fetches:
  - 🪙 Fiat currency rates (`last_currencies.php`)
  - 🪙 Gold rates (`gold_rates.php`)
- Saves data as JSON in the `/data` directory
- 🔄 Auto-updates every 10 minutes via GitHub Actions

## 📂 Project Structure

```
.
├── .github/
│   └── workflows/
│       └── update-data.yml  # GitHub Actions workflow
├── data/
│   ├── fiat.json       # Latest fiat currency data
│   └── gold.json       # Latest gold rate data
├── src
│   └── app.py          # Main script file
├── requirements.txt    # requirements file
```

## 📦 Installation

Clone this repository:

```bash
git clone https://github.com/HosseinOdd/Navasan-API.git
cd Navasan-API
```

## ⚙️ Requirements

- Python 3.7+
- Google Chrome
- ChromeDriver (matching your Chrome version)

### 🔧 Install Dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

Then install required packages:

```bash
pip install -r requirements.txt
```

## 🧪 Usage

Simply run the script:

```bash
python src/app.py
```

✅ The script will:
- Launch a headless browser
- Generate CSRF token using PHPSESSID
- Fetch and store currency/gold data in `data/`

## 📁 Output

- `data/fiat.json`: Fiat currency rates (e.g., USD, EUR, etc.)
- `data/gold.json`: Gold and coin rates in Iran

## 🛡️ Disclaimer

This project is for **educational and personal use only**.  
Please respect the [terms of service](https://www.navasan.net) of the target website.

---

🔗 **Made with ❤️ for automation and data collection**
