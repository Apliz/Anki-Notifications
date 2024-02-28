"""Benchmark module"""
import cProfile
from dotenv import dotenv_values
from main import main
from notification import Notification
from network import Network
from static.constants import URL,REQUESTPATH
from config import REVIEWTOLL,ADDRESSES

envar = dotenv_values(".env")

n = Notification(
            REVIEWTOLL,
            URL,
            envar["PUSHOVER_TOKEN"],
            envar["PUSHOVER_USERKEY"],
            REQUESTPATH
    )
www = Network(ADDRESSES)
cProfile.run("main(n,www)")
