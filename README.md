# MCP Weather App Server

This project is a simple Model Context Protocol (MCP) server that provides real-time weather information for any city using the OpenWeather API. It is built with Python and leverages the FastMCP framework for easy tool integration and API serving.

## Features

- Fetches current weather data for any city worldwide
- Returns temperature, humidity, weather description, wind speed/direction, cloudiness, and more
- Uses OpenWeather's geocoding and weather APIs
- Designed as an MCP tool for easy integration with AI agents and other MCP clients

## Requirements

- Python 3.8+
- [OpenWeather API Key](https://openweathermap.org/api)
- Internet connection

## Installation

1. **Clone the repository:**

   ```sh
   git clone <your-repo-url>
   cd mcp_app_server
   ```

2. **Install dependencies:**
   If using `pip`:

   ```sh
   pip install -r requirements.txt
   ```

   Or, if using `pyproject.toml` (with UV):

   ```sh
   uv install
   ```

   Ensure you have `uv` installed. If not, you can install it via pip:

3. **Set up environment variables:**

    - Create a `.env` file in the project root directory and add your OpenWeather API key:

      ```sh
      echo "OPENWEATHER_API_KEY=your_openweather_api_key_here" > .env
      ```

    - Create a `.env` file in the project root:

     ```env
     OPENWEATHER_API_KEY=your_openweather_api_key_here
     ```

## Usage

Run the server with:

```sh
python main.py
```

The server will start and expose the MCP tool for weather queries.

### Example Tool Usage

The main tool is `get_weather(city: str) -> dict`, which fetches weather data for the specified city.

#### Example Request

```python
from mcp_weather import get_weather
result = get_weather("London")
print(result)
```

#### Example Response

```json
{
  "city": "London",
  "temperature": 18.5,
  "humidity": 65,
  "description": "light rain",
  "icon": "10d",
  "wind_speed": 4.1,
  "wind_direction": 80,
  "cloudiness": 90,
  "timestamp": 1719324000,
  "timezone": 3600,
  "country": "GB"
}
```

## Project Structure

```folder
mcp_app_server/
├── LICENSE
├── main.py            # Entry point to run the MCP server
├── Notes.txt
├── pyproject.toml     # Project metadata and dependencies
├── README.md
├── uv.lock
└── src/
    ├── mcp_weather.py # Weather tool implementation

```

## Environment Variables

- `OPENWEATHER_API_KEY`: Your API key from OpenWeather. Required for the server to fetch weather data.

## Error Handling

- If the API key is missing or invalid, the server will raise an error.
- If the city is not found, a descriptive error is returned.
- Handles unexpected API response formats gracefully.

## Extending

- Add more MCP tools by defining new functions with the `@mcp.tool()` decorator in `src/mcp_weather.py` or new modules.
- Integrate with other MCP-compatible agents or clients as needed.

## 📝 License

This project is [MIT](/LICENSE) licensed.

## Acknowledgments

- [OpenWeather API](https://openweathermap.org/api)
- [FastMCP Framework](https://github.com/modelcontext/fastmcp)
