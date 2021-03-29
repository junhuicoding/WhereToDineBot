import requests
import keys
import json
from types import SimpleNamespace
import logging

# Enable logging
logging.basicConfig(
    filename="log.txt",
    filemode='a',
    format=u'%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

API_KEY = keys.GOOGLE_PLACES_API_KEY
BASE_URL = "https://maps.googleapis.com/maps/api/place/"


def nearyby_search(location: str, parameters: dict) -> json:
    # Set defualt params to look for restaurant types, and is currently operational
    url = BASE_URL + f'nearbysearch/json?key={API_KEY}&types=restaurant&business_status=OPERATIONAL'

    # Add location into query string
    url = f'{url}&location={location}'

    # Add radius, default to 500m if not specified
    if "radius" in parameters:
        url = f'{url}&radius={parameters.get("radius")}'
    else:
        url = f'{url}&radius={500}'

    logger.info("querying: %s", url)
    response = requests.get(url)
    logger.info("Response: %s", response.text)
    response_json = response.json()

    print("HELLO")
    print(response_json.get("results"))

    return response

