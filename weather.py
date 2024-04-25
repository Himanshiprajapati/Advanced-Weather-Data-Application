# app.py
from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()  # Load environment variables from .env file

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        weather_data = get_weather_data(location)
        email_content = generate_email(weather_data)
        # Here you would implement sending the email
        return render_template('email_template.html', email=email_content)
    return render_template('index.html')

def get_weather_data(location):
    """Fetches weather data from WeatherAPI.com"""
    api_key = os.getenv('WEATHER_API_KEY')
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        # Handle errors appropriately
        return None

def generate_email(weather_data):
    """Generates an email content using OpenAI API"""
    openai_key = os.getenv('OPENAI_API_KEY')
    headers = {'Authorization': f'Bearer {openai_key}'}
    prompt = f"Generate a professional email for the weather conditions: {weather_data}"
    response = requests.post('https://api.openai.com/v1/engines/text-davinci-003/completions',
                             json={'prompt': prompt, 'max_tokens': 150}, headers=headers)
    return response.json()['choices'][0]['text'] if response.status_code == 200 else "Error in generating email."

if __name__ == '__main__':
    app.run(debug=True)
