""" Utility Methods \n
    Provides direct access to notification string builder and POST methods
"""
from urllib import parse
from http.client import HTTPSConnection
from dotenv import dotenv_values
from helpers import first_two_names, get_decks_dict
from static.constants import URL,REQUESTPATH
from config import THRESHOLD, COLLECTION

envar = dotenv_values(".env")
col = COLLECTION

def pushover_post(message:str) -> None:
    """
    Sends a notification string via ```HTTPSConnection``` to Pushover \n
    Args:
        message (str) : notification string to be send to pushover
    """
    conn = HTTPSConnection(URL)
    conn.request("POST", REQUESTPATH,
        parse.urlencode({
        "token": envar["PUSHOVER_TOKEN"],
        "user": envar["PUSHOVER_USERKEY"],
        "message": message,
      }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()

def get_learnable_cards() -> tuple[list[str],int]:
    """
    Retrieves the count of reviewable cards and deck names from the Anki Collection
    """
    my_decks = get_decks_dict()
    deck_names = []
    to_review = 0
    for name, _id in my_decks.items():
        count = col.sched.deck_due_tree(_id).review_count
        if count:
            to_review += count
            deck_names.append(f'{name}')
    if to_review > THRESHOLD:
        return deck_names, to_review

def grammar(deck_names:list[str],reviewable_card_count:int) -> str:
    """
    Formats the message string grammar depending on amount of learnable decks \n
    Args:
        deck_names (list[str]) : list of all deck names that have reviewable cards \n
        reviewable_card_count (int) : total count of reviewable cards across all decks
    """
    deck_count = len(deck_names)
    string_base = f'You have {reviewable_card_count} cards ready for review in '
    match deck_count:
        case 1:
            return f'{string_base} {deck_names[0]}'
        case 2:
            return f'{string_base}{first_two_names(deck_names)}'
        case 3:
            return f'{string_base}{first_two_names(deck_names)}{deck_names[2]}'
        case _:
            return f'{string_base}{first_two_names(deck_names)}{deck_count - 2} more'
