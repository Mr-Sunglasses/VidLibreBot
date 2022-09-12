import random
import threading

import requests
from random import randint

api = "https://api.api-ninjas.com/v1/quotes?category="
quotes = []
quote_number = 0


def preload_quotes():
    global quotes
    quotes.clear()
    
    randon_quote = requests.get(api, headers={'X-Api-Key': 'ZSVhux9848gfWCCCLMlESQ==UwDZ4yCxgj0irhQu'}).json()
    content = randon_quote[0]
    author = content["author"]
    quote = content["quote"] + "\n\n" + "By " + author
    quotes.append(quote)

#print(quotes[0])

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
