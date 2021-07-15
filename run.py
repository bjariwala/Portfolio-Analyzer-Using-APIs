import os
from dotenv import load_dotenv
from CB_api import CoinbaseClient
import requests
import json

load_dotenv()
cb_api_key = os.getenv("cb_api")
cb_secret = os.getenv("cb_secret")
cb_passphrase = os.getenv("cb_passphrase")

test = CoinbaseClient(cb_api_key, cb_secret, cb_passphrase)
print(test.historical_data('BTC-USD', 86400))


