from flask import Flask , request , render_template
# from flask_sqlalchemy import SQLAlchemy
import requests
from datetime import datetime
app = Flask(__name__)




   
@app.route('/forecast', methods=['GET'])
def forecast():
    city = request.args.get('city')
    url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"
    querystring = {"city": city}
    headers = {
        "X-RapidAPI-Key": "eea3abff04msh62c8f12f846e8bdp13f022jsn6bf9fc8e698a",
        "X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    weather_data = response.json()
    cloud_pct = weather_data.get("cloud_pct")
    temp = weather_data.get("temp")
    feels_like = weather_data.get("feels_like")
    humidity = weather_data.get("humidity")
    min_temp = weather_data.get("min_temp")
    max_temp = weather_data.get("max_temp")
    wind_speed = weather_data.get("wind_speed")
    wind_degrees = weather_data.get("wind_degrees")
    if "sunrise" in weather_data:
      sunrise_timestamp = weather_data["sunrise"]
      sunrise = datetime.fromtimestamp(sunrise_timestamp).strftime('%Y-%m-%d %H:%M:%S')
    else:
      sunrise = "N/A"
    if "sunset" in weather_data:
       sunset_timestamp = weather_data.get("sunset")
       sunset = datetime.fromtimestamp(sunset_timestamp).strftime('%Y-%m-%d %H:%M:%S')
    else:
      sunset = "N/A"
   
    
    
    return render_template('base.html', city=city, cloud_pct=cloud_pct, temp=temp, feels_like=feels_like, humidity=humidity, min_temp=min_temp, max_temp=max_temp, wind_speed=wind_speed, wind_degrees=wind_degrees, sunrise=sunrise, sunset=sunset)

# @app.route('/')
# def hello():
#          url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"

#          querystring = {"city":"Islamabad"}

#          headers = {
# 	     "X-RapidAPI-Key": "eea3abff04msh62c8f12f846e8bdp13f022jsn6bf9fc8e698a",
# 	     "X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
#          }

#          response = requests.request("GET", url, headers=headers, params=querystring)
#          y= response.json()
#          temp = y["temp"]
#          return temp  

# @app.route('/weather')
# def weather():
#     api_key = "af8132e4c0f44d63d9e8529247190d08"  # Replace "YOUR_API_KEY" with your actual API key
#     city = request.args.get('city', 'Islamabad') # Default to New York if city not specified in query params
#     url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
#     response = requests.get(url)
#     weather_data = response.json()
#     temperature_in_kelvin = weather_data["main"]["temp"]
#     temperature_in_celsius = temperature_in_kelvin - 273.15
#     return f'The temperature in {city} is {temperature_in_celsius} degrees Celsius.'

if __name__ == "__main__":
    app.run(debug=True, port=8000)