"""Import utility function from utils.py"""
from builtins import exit
from utils import get_learnable_cards, pushover_post, grammar
from thread_manager import network

def main():
    """Top level function"""
    network.start()
    deck_names, card_count = get_learnable_cards()
    message = grammar(deck_names, card_count)
    network.join()
    pushover_post(message)

if __name__ == "__main__":
    exit(main())
