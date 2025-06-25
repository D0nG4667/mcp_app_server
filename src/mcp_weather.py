import os
from typing import Any
from mcp.server.fastmcp import FastMCP
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the FastMCP server
mcp = FastMCP("weather", dependencies=["requests"])

@mcp.tool()
def get_weather(city: str) -> dict[str, Any]:  
    """Fetch the current weather for a given city.
    Args:
        city (str): The name of the city to fetch the weather for.
    Returns:
        dict[str, Any]: A dictionary containing the weather information.
    """
    
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        raise ValueError("API key for OpenWeather is not set in the environment variables.")
    
    # Get the latitude and longitude of the city
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api_key}"
    geo_data = requests.get(geo_url).json()
    if not geo_data or "lat" not in geo_data[0] or "lon" not in geo_data[0]:
        raise ValueError(f"Could not find coordinates for city: {city}")
    lat = geo_data[0]["lat"]
    lon = geo_data[0]["lon"]
    
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise ValueError(f"Error fetching weather data: {response.status_code} - {response.text}")
    
    # Check if the response contains the expected data
    data = response.json()
    if "main" not in data or "weather" not in data:
        raise ValueError("Unexpected response format from OpenWeather API.")
    
    weather_info = {
        "city": data.get("name"),
        "temperature": data["main"].get("temp"),
        "humidity": data["main"].get("humidity"),
        "description": data["weather"][0].get("description"),
        "icon": data["weather"][0].get("icon"),
        "wind_speed": data["wind"].get("speed"),
        "wind_direction": data["wind"].get("deg"),
        "cloudiness": data["clouds"].get("all"),
        "timestamp": data.get("dt"),
        "timezone": data.get("timezone"),
        "country": data.get("sys", {}).get("country"),
    }
    
    return weather_info

if __name__ == "__main__":
    mcp.run()
    
    
    
    