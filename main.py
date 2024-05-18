import argparse
import pyfiglet
from simple_chalk import chalk
import requests
import os
from dotenv import load_dotenv
load_dotenv()

# API key for openweathermap
API_KEY = os.getenv('API_KEY')

# Base URL for openweathermap
BASE_URL = os.getenv('BASE_URL')

# Map the weather codes to weather icons
WEATHER_ICONS = {
    # day icons
    "01d": "☀️",
    "02d": "⛅",
    "03d": "☁️",
    "04d": "☁️",
    "09d": "🌧️",
    "10d": "🌦️",
    "11d": "⛈️",
    "13d": "🌨️",
    "50d": "💨",
    # night
    "01n": "🌙",
    "02n": "⛅",
    "03n": "☁️",
    "04n": "☁️",
    "09n": "🌧️",
    "10n": "🌦️",
    "11n": "⛈️",
    "13n": "🌨️",
    "50n": "💨",
}

# Construct API URL with query parameters
parser = argparse.ArgumentParser(description="Check the weather for a certain country/city")
parser.add_argument("country", help="The country/city to check the weather")

args = parser.parse_args()

url = f"{BASE_URL}?q={args.country}&appid={API_KEY}&units=imperial"

# Make API request and parse response using requests module

response = requests.get(url)

if response.status_code != 200:
    print(chalk.red("Error: Unable to retrieve weather information"))
    exit()

# Parsing the JSON response from the API, extract the weather information
data = response.json()

# Get information from response

temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
description = data["weather"][0]["description"]
icon = data["weather"][0]["icon"]
city = data["name"]
country = data["sys"]["country"]

# Construct the output

weather_icon = WEATHER_ICONS.get(icon, "")
output = f"{pyfiglet.figlet_format(city)}, {country}\n\n"
output += f"{weather_icon} {description}\n"
output += f"Temperature: {temperature}°F\n"
output += f"Feels like: {feels_like}°F\n"

# Print the output
print(chalk.green(output))
