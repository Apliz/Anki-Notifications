"""Helper Functions"""
from time import sleep
from requests import Timeout, head, ConnectionError
from config import ADDRESSES
from static.constants import COLLECTIONPATH

# For some reason on HOME network 10.0.0.1 and 8.8.8.8 do not fucntion
# Strangely 1.1.1.1 DOES function.
def network_listener():
    """Listens for an active network"""
    result = None
    while result is None:
        for ip in ADDRESSES:
            print(ip)
            try:
                print("where are we getting hung up?")
                result = head(f'http://{ip}', timeout=1)
                print(result)
                if result is not None:
                    return
            except (ConnectionError, Timeout):
                print("in the except")
                sleep(2)

def first_two_names(deck_names) -> str:
    """Returns correct grammar for the first two deck names"""
    n = len(deck_names)
    if n < 3:
        return f'{deck_names[0]} and {deck_names[1]}'
    elif n > 2:
        return f'{deck_names[0]}, {deck_names[1]}, and '

def get_decks_dict() -> dict:
    """Returns python dictionary of Anki decks"""
    my_decks = {}
    col = COLLECTIONPATH
    for deck in col.decks.all_names_and_ids():
        my_decks[deck.name] = deck.id
    my_decks.popitem()
    return my_decks
    