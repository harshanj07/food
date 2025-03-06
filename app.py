from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = '57670bd466msh428457352101b22p197e35jsnff03294b700c'
API_URL = 'https://yahoo-weather5.p.rapidapi.com/weather'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        city_name = request.form['city_name']
        print(f"Received city name: {city_name}")  # Debug statement
        headers = {
            'x-rapidapi-host': "yahoo-weather5.p.rapidapi.com",
            'x-rapidapi-key': API_KEY
        }
        params = {
            'location': city_name,
            'format': 'json',
            'u': 'f'
        }
        response = requests.get(API_URL, headers=headers, params=params)
        print(f"API response status: {response.status_code}")  # Debug statement
        if response.status_code == 200:
            weather = response.json()
            print(f"API response data: {weather}")  # Debug statement
        else:
            print(f"Error: {response.text}")  # Debug statement for error
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True, port=5545)