"""Helper Functions"""
from time import sleep
from requests import Timeout, head, ConnectionError
from anki.collection import Collection
from constants import COLLECTIONPATH

def network_listener() -> None:
    """Listens for an active network"""
    ip_addresses, result = ["1.1.1.1", "8.8.8.8", "10.0.0.1"], None
    while result is None:
        print("in network_listener() WHILE")
        for ip in ip_addresses:
            print("in network_listener() FOR")
            try:
                print("in network_listener() TRY BEFORE HEAD()")
                result = head(f'http://{ip}', timeout=2)
                print("in network_listener() AFTER HEAD")
                if result is not None:
                    print("in network_listener() EXCEPT")
                    return
            except (ConnectionError, Timeout):
                sleep(2)


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
