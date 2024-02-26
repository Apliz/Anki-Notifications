""" Helper Methods \n
    Container for all methods called by utils.py
"""
from time import process_time, asctime
from requests import head, Timeout, ConnectionError
from config import NETWORKTIMEOUT

class Network():
    """Network Manager"""
    def __init__(self, ip_list):
        self.ip_list=ip_list


    async def establish_connection (self, result = None) -> bool:
        """ Loops through a list of given IP passing them to net_conn() to attempt the connection"""
        timeout = self.maxwait()
        while result is None:
            for ip in self.ip_list:
                if self.net_conn(ip, timeout):
                    return

    @staticmethod
    def maxwait() -> int:
        """ Returns the timeout time/s for ```network_listener()```"""
        timeout=0
        timeout += NETWORKTIMEOUT[0] * 3600
        timeout += NETWORKTIMEOUT[1] * 60
        timeout += NETWORKTIMEOUT[2]
        return timeout

    @staticmethod
    def write_log(timeout) -> None:
        """
            writes network error timeout to log
        """
        with open("./static/log.txt",mode="a",encoding="utf-8",newline="",closefd=True) as f:
            f.write(f'[network_listener(), at date: {asctime()}, message: timeout was exceed. timeout was set to: {timeout} seconds]\n')
            f.close()

    @staticmethod
    def net_conn(ip, timeout) -> bool|None:
        """Attempts connection to the www. Exits program if none is found"""
        try:
            result = head(f'http://{ip}', timeout=1).status_code
            if result == 301:
                return True
        except (ConnectionError, Timeout):
            if process_time() > timeout:
                Network.write_log(timeout)
                exit()
