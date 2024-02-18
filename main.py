"""Import utility function from utils.py"""
import sys
from utils import create_message, pushover_post
from helpers import has_internet_connection

def main():
    """Top level function"""
    if has_internet_connection():
        message = create_message()
        pushover_post(message)
        return 0


if __name__ == "__main__":
    sys.exit(main())
