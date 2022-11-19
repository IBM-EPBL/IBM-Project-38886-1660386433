from flask import Flask, request, render_template
import requests
from flask import Flask, request, render_template
import requests

app = Flask(_name_)


@app.route('/', methods=["GET", "POST"])
def index():
    weatherData = ''
    error = 0
    cityName = ''
    if request.method == "POST":
        cityName = request.form.get("cityName")
        if cityName:
            weatherApiKey = '3f5d38932ad9ae0caa0302a35fbc8496'
            url = "https://api.openweathermap.org/data/2.5/weather?q=" + cityName + "&appid=" + weatherApiKey
            weatherData = requests.get(url).json()
        else:
            error = 1
    return render_template('index.html', data=weatherData, cityName=cityName, error=error)


if _name_ == "_main_":
    app.run()

app = Flask(_name_)


@app.route('/', methods=["GET", "POST"])
def index():
    weatherData = ''
    error = 0
    cityName = ''
    if request.method == "POST":
        cityName = request.form.get("cityName")
        if cityName:
            weatherApiKey = '3f5d38932ad9ae0caa0302a35fbc8496'
            url = "https://api.openweathermap.org/data/2.5/weather?q=" + cityName + "&appid=" + weatherApiKey
            weatherData = requests.get(url).json()
        else:
            error = 1
    return render_template('index.html', data=weatherData, cityName=cityName, error=error)


if _name_ == "_main_":
    app.run(