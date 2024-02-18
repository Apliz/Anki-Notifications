"""Helper Functions"""
import requests
from anki.collection import Collection
from constants import COLLECTIONPATH

def has_internet_connection() -> bool | ConnectionError:
    """Check for active internet connection"""
    ip_addresses = ["1.1.1.1", "8.8.8.8", "10.0.0.1"] 
    for ip in ip_addresses:
        try:
            requests.get(f'http://{ip}', timeout=1)     
            return True
        except (requests.ConnectionError, requests.Timeout):
            continue
    raise ConnectionError("No connection to the internet was detected")

def get_collection():
    """Establish connection to collection.anki2 file"""
    return Collection(COLLECTIONPATH)

def grammar():
    """Formats the message string grammar depending on amount of learnable decks"""
    # Still to implement:
    #     1. deck name grammar switch function to allow for different list length:
    #       a. 'name1'
    #       b. 'name 1 and name2
    #       c. 'name1, name2 and name3
    #       d. 'name1, name2 and X other decks
    return None
