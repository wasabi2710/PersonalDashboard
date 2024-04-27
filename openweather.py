import requests
from gps import get_current_gps_coordinates

KEY = "3351188f7b1376edc336e01494e50898"
coordinate = get_current_gps_coordinates()
LAT, LONG = coordinate

def fetch_weather_data():
    """
    Fetches weather data for the predefined latitude and longitude using the OpenWeatherMap API.
    
    Returns:
    dict: A dictionary containing the weather data or an error message.
    """
    # Formatting the URL using the predefined constants
    my_rest = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LONG}&appid={KEY}"
    
    # Making the request
    rep = requests.get(my_rest)
    if rep.status_code == 200:
        weather = rep.json()
        
        # Extracting and processing the required information
        city_name = weather['name']
        weather_description = weather['weather'][0]['description']
        wind_speed = weather['wind']['speed']
        
        # Converting temperature from Kelvin to Celsius
        temp_kelvin = weather['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        
        
        # Returning the extracted information as a dictionary
        return {
            "city_name": city_name,
            "weather_description": weather_description,
            "wind_speed": wind_speed,
            "temperature_celsius": temp_celsius,
        }
    else:
        return {"error": f"Error: {rep.status_code}"}

# # Example usage:
# weather_data = fetch_weather_data()
# print(weather_data)
# print(f"{LAT} and {LONG}")
