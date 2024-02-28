"""Top level module: main.py"""
from builtins import exit
from asyncio import run
from dotenv import dotenv_values
from network import Network
from notification import Notification
from static.constants import URL,REQUESTPATH
from config import REVIEWTOLL,ADDRESSES

envar = dotenv_values(".env")

async def main(notification, network) -> None:
    """Control flow method"""
    conn = network.establish_connection()
    message = notification.compose()
    await conn
    notification.post(message)

if __name__ == "__main__":
    n = Notification(
            REVIEWTOLL,
            URL,
            envar["PUSHOVER_TOKEN"],
            envar["PUSHOVER_USERKEY"],
            REQUESTPATH
    )
    www = Network(ADDRESSES)
    exit(run(main(n, www)))
