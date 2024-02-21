"""Import utility function from utils.py"""
# from sys import
from builtins import exit
from utils import get_learnable_cards, pushover_post, grammar
from helpers import network_listener

def main():
    """Top level function"""

    while not network_listener():
        print("in the while")
        deck_names, card_count = get_learnable_cards()
        message = grammar(deck_names, card_count)
        pushover_post(message)
        return 0
    print("outside the while")

if __name__ == "__main__":
    exit(main())
