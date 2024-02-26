""" Helper Methods \n
    Container for all methods called by utils.py
"""
from time import process_time, asctime
from requests import Timeout, head, ConnectionError
from config import ADDRESSES, COLLECTION, NETWORKTIMEOUT

async def network_listener(result = None) -> bool:
    """ Loops through a list of given IP 
        addresses and returns ```True``` once an active connection is established \n
        If no active connection is detected after value ```MAXWAIT``` (time in seconds)
        the method returns ```False```
    """
    timeout = maxwait()
    while result is None:
        for ip in ADDRESSES:
            if net_conn(ip, timeout):
                return

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

def maxwait() -> int:
    """ Returns the timeout time/s for ```network_listener()```"""
    timeout=0
    timeout += NETWORKTIMEOUT[0] * 3600
    timeout += NETWORKTIMEOUT[1] * 60
    timeout += NETWORKTIMEOUT[2]
    return timeout

def write_log(timeout):
    """
        writes network_listener timeout to log
    """
    with open("log.txt",mode="a",encoding="utf-8",newline="",closefd=True) as f:
        f.write(f'[network_listener(), at date: {asctime()}, message: timeout was exceed. timeout was set to: {timeout} seconds]\n')
        f.close()

def net_conn(ip, timeout):
    """Attempts connection to the www"""
    try:
        result = head(f'http://{ip}', timeout=1).status_code
        if result == 301:
            return True
    except (ConnectionError, Timeout):
        if process_time() > timeout:
            write_log(timeout)
            exit()
