
# Ako nemate flask onda sljedeća naredba u terminalu:
# pip install -r requirements.txt 
# Ako javlja grešku za requests onda sljedeća naredba u terminalu::
# pip3 install requests 

import json
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():

    query = "London,UK"
    unit = "metric"
    api_key = "" #unesite svoj API ključ!

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}&lang=HR".format(query, unit, api_key)

    data = requests.get(url=url) # GET zahtjev kojeg šaljemo na stranicu open weather

    return render_template("index.html", data=data.json())


if __name__ == "__main__":
    app.run()