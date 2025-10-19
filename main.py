import requests
import os
from dotenv import load_dotenv
load_dotenv()


TOKEN = os.getenv("TOKEN")

def get_holidays():
    params = {
        "api_key": TOKEN,
        "country": "by",
        "year": "2025"
    }
    api_url = "https://calendarific.com/api/v2/holidays"
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    holidays = response.json()["response"]["holidays"]
    return holidays

def main():
    holidays = get_holidays()
    months = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
    for holiday in holidays:
        print(f"""
        Дата:{holiday['date']['datetime']['day']} {months[holiday['date']['datetime']['month']-1]}
        Название праздника: {holiday['name']}
        Описание: {holiday['description']}""")


if __name__ == '__main__':
    main()