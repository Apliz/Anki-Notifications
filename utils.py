""""""
import urllib
import http.client
from anki.collection import Collection
from dotenv import dotenv_values

config = dotenv_values(".env")
col = Collection(config["COLLECTIONPATH"])
URL= "api.pushover.net:443"
REQUESTPATH = "/1/messages.json"

# Why on earth do I need to pop off the last dictionary item for it to work?
# The only clue that I have is that it adds filtered lists, need to find a
# general solution to fix this.

def get_decks_dict():
    """Returns python dictionary of Anki decks"""
    my_decks = {}
    for deck in col.decks.all_names_and_ids():
        my_decks[deck.name] = deck.id
    my_decks.popitem()
    return my_decks


def pushover_post(message):
    """POST notifaction message string to Pushover"""
    conn = http.client.HTTPSConnection(URL)
    conn.request("POST", REQUESTPATH,
      urllib.parse.urlencode({
        "token": config["PUSHOVER_TOKEN"],
        "user": config["PUSHOVER_USERKEY"],
        "message": message,
      }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()
    return 1

# Still to implement:
# 1. deck name grammar switch function to allow for different list length:
#     a. 'name1'
#     b. 'name 1 and name2
#     c. 'name1, name2 and name3
#     d. 'name1, name2 and X other decks

def create_message():
    """GET and validate message data from 'collection.anki2' """
    my_decks = get_decks_dict()
    deck_names = ""
    review_total = 0
    for name, _id in my_decks.items():
        count = col.sched.deck_due_tree(_id).review_count
        if count:
            review_total += count
            deck_names += f'{name},'
    if review_total > 0:
        message_string=f'You have {review_total} cards ready to be learned in {deck_names}today!'
        return message_string
