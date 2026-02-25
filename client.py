import requests

api_url = "https://opensky-network.org/api/tracks/all?icao24=e49ef0&time=0"

response = requests.get(api_url)
print(response.text)