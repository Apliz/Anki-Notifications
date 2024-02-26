"""Top level module: main.py"""
from builtins import exit
from asyncio import run
from dotenv import dotenv_values
from network import Network
from notification import Notification
from static.constants import URL,REQUESTPATH
from config import REVIEWTOLL, COLLECTION,ADDRESSES

envar = dotenv_values(".env")

async def main() -> None:
    """Control flow method"""
    www = Network(ADDRESSES)
    n = Notification(
            REVIEWTOLL,
            COLLECTION,
            URL,
            envar["PUSHOVER_TOKEN"],
            envar["PUSHOVER_USERKEY"],
            REQUESTPATH
    )
    message = n.compose()
    await www.establish_connection()
    n.send(message)

if __name__ == "__main__":
    exit(run(main()))
