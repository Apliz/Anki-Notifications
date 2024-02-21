"""Threading and Queue Manager"""
from threading import Thread
from helpers import network_listener

network = Thread(group=None, target=network_listener,name="Thread01")
