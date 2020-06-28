from flask import Flask, render_template, request, url_for, flash, redirect
import requests
import pprint

app = Flask(__name__)

IP = '131.114.137.91'
PORT = '8080'


@app.route('/schedule')
def schedule():
    url = 'http://{}:{}/v1/{}'.format(IP, PORT, 'schedules')
    schedules = requests.get(url)
    pprint.pprint(schedules.json())
    return render_template('schedules.html', schedules=schedules.json())


@app.route('/')
def index():
    print(request.endpoint)
    return redirect('/schedule')
