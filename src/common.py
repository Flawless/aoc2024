import requests
import os

SESSION_TOKEN = os.getenv("SESSION_TOKEN")  # Replace with your session token
BASE_URL = "https://adventofcode.com/2024/day/{}/input"


def fetch_puzzle_input(day_number):
    url = BASE_URL.format(day_number)
    headers = {"Cookie": f"session={SESSION_TOKEN}", "User-Agent": "Python script"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an error if the request failed
    return response.text
