"""Import utility function from utils.py"""
from asyncio import to_thread, run
from builtins import exit
from utils import get_learnable_cards, pushover_post, grammar
from helpers import network_listener

async def main():
    """Top level function"""
    network = to_thread(network_listener)
    deck_names, card_count = get_learnable_cards()
    message = grammar(deck_names, card_count)
    await network
    pushover_post(message)

if __name__ == "__main__":
    exit(run(main()))
