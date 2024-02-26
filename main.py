"""Top level module: main.py"""
from builtins import exit
from asyncio import run
from utils import get_learnable_cards, pushover_post, grammar
from helpers import network_listener

async def main() -> None:
    """Control flow method"""
    deck_names, card_count = get_learnable_cards()
    message = grammar(deck_names, card_count)
    await network_listener()
    pushover_post(message)

if __name__ == "__main__":
    exit(run(main()))
