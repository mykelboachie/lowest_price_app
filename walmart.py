## Walmart API for importing product information
## Requires 'Key' which is kept in a separate doc for security


from wapy.api import Wapy


def open_key(key_text_name):
    # Open key text file
    with open(key_text_name) as api_key_text:
        key = api_key_text.readline()

    return key


def start_API():
    # start api instance
    wapy = Wapy(open_key("walmart_key.txt"))
    return wapy


