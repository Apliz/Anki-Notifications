"""Import utility function from utils.py"""
from utils import create_message, pushover_post

def main():
    """Top level function"""
    # If internet connection = TRUE
    #   generate post data with generate_post()
    #   Pass data to pushover_post and execute
    message = create_message()
    pushover_post(message)

if __name__ == "__main__":
    main()

# generate_post_data()
