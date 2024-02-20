"""Utility files"""
from urllib import parse
from http.client import HTTPSConnection
from dotenv import dotenv_values
from helpers import get_collection, first_two_names
import constants as const

config = dotenv_values(".env")
col = get_collection()

# Why on earth do I need to pop off the last dictionary item for it to work?

# The only clue that I have is that anki will append a filtered list item 
# to the end of the all_names_ids(), need to find a general solution to fix this.
def get_decks_dict() -> dict:
    """Returns python dictionary of Anki decks"""
    my_decks = {}
    for deck in col.decks.all_names_and_ids():
        my_decks[deck.name] = deck.id
    my_decks.popitem()
    return my_decks

def pushover_post(message):
    """POST notifaction message string to Pushover"""
    conn = HTTPSConnection(const.URL)
    conn.request("POST", const.REQUESTPATH,
        parse.urlencode({
        "token": config["PUSHOVER_TOKEN"],
        "user": config["PUSHOVER_USERKEY"],
        "message": message,
      }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()
    return 1

def get_learnable_cards():
    """GET and validate message data from 'collection.anki2' """
    my_decks = get_decks_dict()
    deck_names = []
    learnable_card_count = 0
    for name, _id in my_decks.items():
        count = col.sched.deck_due_tree(_id).review_count
        if count:
            learnable_card_count += count
            deck_names.append(f'{name}')
    if learnable_card_count > 0:
        return deck_names, learnable_card_count

# I want to make the notification more clear.
# Some research would be good here.
def grammar(deck_names,learnable_card_count):
    """Formats the message string grammar depending on amount of learnable decks"""
    deck_count = len(deck_names)
    string_base = f'You have {learnable_card_count} cards ready for review in '
    match deck_count:
        case 1:
            return f'{string_base} {deck_names[0]}'
        case 2:
            return f'{string_base}{first_two_names(deck_names)}'
        case 3:
            return f'{string_base}{first_two_names(deck_names)}{deck_names[2]}'
        case _:
            return f'{string_base}{first_two_names(deck_names)}{deck_count - 2} more'
    return None
