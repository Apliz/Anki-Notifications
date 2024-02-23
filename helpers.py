""" Helper Methods \n
    Container for all methods called by utils.py
"""
from time import sleep
from requests import Timeout, head, ConnectionError
from config import ADDRESSES, COLLECTION

# For some reason on HOME network 10.0.0.1 and 8.8.8.8 do not fucntion
# Strangely 1.1.1.1 DOES function.
def network_listener() -> bool:
    """ Loops through a list of given IP 
        addresses and returns ```True``` once an active connection is established \n
        If no active connection is detected after value ```MAXWAIT``` (time in seconds)
        the method returns ```False```
    """
    result = None
    while result is None:
        for ip in ADDRESSES:
            print(ip)
            try:
                result = head(f'http://{ip}', timeout=1)
                if result is not None:
                    return
            except (ConnectionError, Timeout):
                continue

def first_two_names(deck_names:list[str]) -> str:
    """ Changes the grammar of the first two names of the notication string,
        depending on the total decks containing reviewable cards \n
        Returns a grammatically correct partial notification string \n
        Args:
            deck_names (list[str]) : list of decks names

    """
    n = len(deck_names)
    if n < 3:
        return f'{deck_names[0]} and {deck_names[1]}'
    elif n > 2:
        return f'{deck_names[0]}, {deck_names[1]}, and '

def get_decks_dict() -> dict[str,int]:
    """Returns a ```dict``` of Anki decks names and their ID"""
    my_decks = {}
    col = COLLECTION
    for deck in col.decks.all_names_and_ids(skip_empty_default=True):
        my_decks[deck.name] = deck.id
    print(my_decks)
    return my_decks
