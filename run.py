import os
from dotenv import load_dotenv
from CB_api import CoinbaseClient
import requests
import json
import sys
from os.path import join, dirname
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = join(dirname(__file__), './/.idea//inspectionProfiles//.env')
print(dotenv_path)
load_dotenv(Path(dotenv_path))

cb_api_key = os.getenv("cb_api_key")
cb_secret = os.getenv("cb_secret")
cb_passphrase = os.getenv("cb_passphrase")
print('-----', cb_api_key, cb_secret, cb_passphrase)
test = CoinbaseClient(cb_api_key, cb_secret, cb_passphrase)
print(test.historical_data('BTC-USD', 86400))


