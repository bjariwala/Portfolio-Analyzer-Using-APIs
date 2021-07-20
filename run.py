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

alpaca_api_key = os.getenv("alpaca_trade_api")
alpaca_secret_key = os.getenv("alpaca_secret_key")

api = tradeapi.REST(
    alpaca_api_key,
    alpaca_secret_key,
    api_version = "v2"
)
ticker = "SPY"

timeframe = "1D"

start_date = pd.Timestamp("2015-05-04", tz="America/New_York").isoformat()
end_date = pd.Timestamp("2020-05-04", tz="America/New_York").isoformat()


