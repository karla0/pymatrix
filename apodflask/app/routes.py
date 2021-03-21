# used for managing endpoints
import datetime
import json
from flask import render_template
import requests
from app import app


API_KEY = 'MzabBeAiCVcA8ZHLnP5a132aNRYMTevN2w3nPH5s'

def set_image_url(data):
    if data.get('hdurl'):
        url = data.get('hdurl')
    else:
        url = data.get('url')
    
    return url


@app.route('/')
@app.route('/today')
def picture_of_day():
    response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={ API_KEY }')
    # data dict
    data = response.json()
    # two urls are included 1 HD and 1 non hd will look for hdurl first
    # then url unsure if this is that necessary yet but just in case.
    url = set_image_url(data)

    return render_template('views/main.html', image=data, image_url=url)

@app.route('/yesterday')
def picture_of_yesterday():
    # using time deltas to make it easier to add or subtract days more
    # easily less change of error
    today = datetime.date.today()
    take_a_day = datetime.timedelta(hours=24)
    yesterday = today - take_a_day
    response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={API_KEY}&date={yesterday}') 
    data = response.json()
    url = set_image_url(data)
    
    return render_template('views/main.html', image=data, image_url=url)

# TODO Create and Beyond funtion which will take the current object that it contains and subtracts 1 from the date and requests the next picture