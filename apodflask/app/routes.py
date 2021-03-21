# used for managing endpoints
import requests
import json
from flask import render_template
from app import app

API_KEY = 'MzabBeAiCVcA8ZHLnP5a132aNRYMTevN2w3nPH5s'
    
@app.route('/')
@app.route('/today')
def picture_of_day():
    response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={ API_KEY }')
    data = response.json()
    # gets image date from response
    date = data.get('date')
    # gets image explanation from response
    explanation = data.get('explanation')
    # gets image title
    image_title = data.get('title')
    # two urls are included 1 HD and 1 non hd will look for hdurl first
    # then url unsure if this is that necessary yet but just in case.
    if data.get('hdurl'):
        url = data.get('hdurl')
    else:
        url = data.get('url')

    return render_template('index.html', title=image_title,date= date, 
                            explanation=explanation, url=url)