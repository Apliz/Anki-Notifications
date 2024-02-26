"""Notification Class"""
from urllib import parse
from http.client import HTTPSConnection

class Notification():

    """builds notifications"""
    def __init__(self, toll, col, url, token, user, request_path):
        self.toll = toll
        self.col  = col
        self.url = url
        self.token = token
        self.user = user
        self.path = request_path

    def compose(self):
        """instance method: build notification"""
        deck_names, card_count = self.get_learnable_cards(self.toll)
        message = self.grammar(deck_names, card_count)
        return message

    def send(self,message:str) -> None:
        """
        Sends a notification string via ```HTTPSConnection``` to Pushover \n
        Args:
            message (str) : notification string to be send to pushover
        """
        conn = HTTPSConnection(self.url)
        conn.request("POST", self.path,
            parse.urlencode({
            "token": self.token,
            "user": self.user,
            "message": message,
          }), { "Content-type": "application/x-www-form-urlencoded" })
        conn.getresponse()

    def get_learnable_cards(self,toll) -> tuple[list[str],int]:
        """Retrieves the count of reviewable cards and deck names from the Anki Collection"""
        my_decks = self.get_decks_dict()
        deck_names = []
        to_review = 0
        for name, _id in my_decks.items():
            count = self.col.sched.deck_due_tree(_id).review_count
            if count:
                to_review += count
                deck_names.append(f'{name}')
        if to_review > toll:
            return deck_names, to_review

    def grammar(self,deck_names:list[str],reviewable_card_count:int) -> str:
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
                return f'{string_base}{self.first_two_names(deck_names)}'
            case 3:
                return f'{string_base}{self.first_two_names(deck_names)}{deck_names[2]}'
            case _:
                return f'{string_base}{self.first_two_names(deck_names)}{deck_count - 2} more'

    def first_two_names(self,deck_names:list[str]) -> str:
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

    def get_decks_dict(self) -> dict[str,int]:
        """Returns a ```dict``` of Anki decks names and their ID"""
        my_decks = {}
        for deck in self.col.decks.all_names_and_ids(skip_empty_default=True):
            my_decks[deck.name] = deck.id
        return my_decks
