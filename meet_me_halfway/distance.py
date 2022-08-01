from datetime import datetime
import requests
import urllib

import pytz

from _credentials import DISTANCE_API_KEY


def compute_distance(start: str, end: str, arrive_at: datetime) -> str:

    standard_query = "https://maps.googleapis.com/maps/api/distancematrix"
    origins = start
    destinations = end
    units = "imperial"
    arrival_time = arrive_at
    language = "fr"
    api_key = str(DISTANCE_API_KEY)

    parameters = {
        "origins": urllib.parse.quote_plus(origins),
        "destinations": urllib.parse.quote_plus(destinations),
        "units": units,
        "language": language,
        "arrival_time": int(arrival_time.replace(tzinfo=pytz.utc).timestamp()),
        "mode": "transit",
        "transit_mode": "bus|tram|subway",
        "transit_routing_preference": "fewer_transfers",
        "key": api_key,
    }
    parameters_in_query = "&".join([f"{k}={v}" for k, v in parameters.items()])

    url = f"{standard_query}/json?{parameters_in_query}"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.text


if __name__ == "__main__":
    test = compute_distance(
        "4 Rue de Sèvres, 75006 Paris, France",
        "15-17 Rue du Buisson Saint-Louis, 75010 Paris, France",
        datetime(2022, 8, 5, 18, 0, 0),
    )
