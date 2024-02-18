"""Import utility function from utils.py"""
import sys
from utils import get_learnable_cards, pushover_post, grammar
from helpers import has_internet_connection

def main():
    """Top level function"""
    if has_internet_connection():
        deck_names, card_count = get_learnable_cards()
        message = grammar(deck_names, card_count)
        pushover_post(message)
        return 0

if __name__ == "__main__":
    sys.exit(main())
