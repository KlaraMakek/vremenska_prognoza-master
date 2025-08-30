# If Flask is not installed, run:
# pip install -r requirements.txt 
# If you get an error with requests, run:
# pip3 install requests 

import json
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    # Default city and API setup
    query = "London,UK"
    unit = "metric"
    api_key = ""  # Insert your API key here

    url = f"https://api.openweathermap.org/data/2.5/weather?q={query}&units={unit}&appid={api_key}&lang=HR"

    response = requests.get(url=url)
    data = response.json()

    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run()
