import random
import threading

import requests
from random import randint

api = "http://api.quotable.io/random"
quotes = []
quote_number = 0


def preload_quotes():
    global quotes

    for x in range(10):
        randon_quote = requests.get(api).json()
        content = randon_quote["content"]
        author = randon_quote["author"]
        quote = content + "\n\n" + "By" + author
        quotes.append(quote)


# preload_quotes()
#
# def random_quote():
#
#      global quotes
#      global quote_number
#
#      return quotes[randint(1,19)]
#
#      quote_number = quote_number + 1
#
#      if quotes[quote_number] == quotes[-3]:
#          thread = threading.Thread(target=preload_quotes)
#          thread.start()
