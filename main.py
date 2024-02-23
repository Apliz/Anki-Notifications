"""Top level module: main.py"""
from builtins import exit
from utils import get_learnable_cards, pushover_post, grammar
from helpers import network_listener

def main() -> None:
    """Control flow method"""
    # deck_names, card_count = get_learnable_cards() 
    # while not network_listener():
    #     message = grammar(deck_names, card_count)
    #     pushover_post(message)

    # Currently the script turns into an infinite loop sending notifications every second.
    # Keep main() disabled until problem is fixed

if __name__ == "__main__":
    exit(main())
``