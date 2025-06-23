from flask import Flask, jsonify, request, render_template
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests for JavaScript

# Your Weather API key (replace with your actual API key)
API_KEY = '233489709a444120ad4130142240207'

# Serve the index.html for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint to get the weather for a city
@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "No city provided"}), 400

    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "Could not fetch weather data"}), 500

    weather_data = response.json()
    temp_celsius = weather_data["current"]["temp_c"]

    return jsonify({
        "city": city,
        "temperature": temp_celsius,
        "weather": weather_data["current"]["condition"]["text"]
    })

if __name__ == '__main__':
    app.run(debug=True)
