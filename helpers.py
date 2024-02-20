"""Helper Functions"""
from builtins import ConnectionError
from requests import get, Timeout
from anki.collection import Collection
from constants import COLLECTIONPATH

def has_internet_connection() -> bool | ConnectionError:
    """Check for active internet connection"""
    ip_addresses = ["1.1.1.1", "8.8.8.8", "10.0.0.1"] 
    for ip in ip_addresses:
        try:
            get(f'http://{ip}', timeout=1)     
            return True
        except (ConnectionError,Timeout):
            continue
    raise ConnectionError("No connection to the internet was detected")

def get_collection():
    """Establish connection to collection.anki2 file"""
    return Collection(COLLECTIONPATH)

def first_two_names(deck_names) -> str:
    """Returns correct grammar for the first two deck names"""
    n = len(deck_names)
    if n < 3:
        return f'{deck_names[0]} and {deck_names[1]}'
    elif n > 2:
        return f'{deck_names[0]}, {deck_names[1]}, and '
