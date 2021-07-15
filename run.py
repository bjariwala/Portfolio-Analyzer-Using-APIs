import os
# from dotenv import load_dotenv
from CB_api import CoinbaseClient
from api_keys import api, secret, passphrase
import requests
import json

test = CoinbaseClient(api, secret, passphrase)
print(test.historical_data('DOGE-USD', 86400))


