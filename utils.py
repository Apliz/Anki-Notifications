from anki.collection import Collection
from dotenv import dotenv_values
import urllib, http.client

config = dotenv_values(".env")

col = Collection(config["COLLECTIONPATH"])
url= "api.pushover.net:443"
request_path = "/1/messages.json"

def get_decks_dict():
  Decks = {
    "Classics" : int(config["DECKID_CLASSICS"]),
    "Physics" : int(config["DECKID_PHYSICS"]),
    "Single_maths" : int(config["DECKID_SINGLEMATHS"]),
    "Further_maths" : int(config["DECKID_FURTHERMATHS"])
  }
  return Decks

def post_to_phone(message):
  conn = http.client.HTTPSConnection(url)
  conn.request("POST", request_path,
    urllib.parse.urlencode({
      "token": config["PUSHOVER_TOKEN"],
      "user": config["PUSHOVER_USERKEY"],
      "message": message,
    }), { "Content-type": "application/x-www-form-urlencoded" })
  conn.getresponse()

def generate_post():
  
  Decks = get_decks_dict()
  deck_names = ""
  total_learnable = 0

  for deck in Decks:
    count = col.sched.deck_due_tree(Decks[deck]).review_count
    if count:
      total_learnable += count
      deck_names += f'{deck},'
  
  if total_learnable:
    post_to_phone(f'You have {total_learnable} cards ready to be learned in {deck_names}today!')

  return None
  