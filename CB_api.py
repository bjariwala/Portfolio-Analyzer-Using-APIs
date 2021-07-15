import json, hmac, hashlib, time, requests, base64
from requests.auth import AuthBase
import pandas as pd
from typing import DefaultDict, Deque, List, Dict, Tuple, Optional, Any


class CBProAuth(AuthBase):
    def __init__(self, api_key, secret_key, passphrase):
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase

    def __call__(self, request):
        timestamp = str(time.time())
        message = ''.join([timestamp, request.method,
                           request.path_url, (request.body or '')])
        request.headers.update(get_auth_headers(timestamp, message,
                                                self.api_key,
                                                self.secret_key,
                                                self.passphrase))
        return request


def get_auth_headers(timestamp, message, api_key, secret_key, passphrase):
    message = message.encode('ascii')
    hmac_key = base64.b64decode(secret_key)
    signature = hmac.new(hmac_key, message, hashlib.sha256)
    signature_b64 = base64.b64encode(signature.digest()).decode('utf-8')
    return {
        'Content-Type': 'Application/JSON',
        'CB-ACCESS-SIGN': signature_b64,
        'CB-ACCESS-TIMESTAMP': timestamp,
        'CB-ACCESS-KEY': api_key,
        'CB-ACCESS-PASSPHRASE': passphrase
    }


class CoinbaseClient:
    def __init__(self, api, secret, passphrase):
        self.auth = CBProAuth(api, secret, passphrase)
        self.url = 'https://api.pro.coinbase.com/'

    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Any:
        r = requests.get(self.url + path, auth=self.auth).json()
        return r

    def historical_data(self, pair, timeframe):
        info = self.get(f'products/{pair}/candles', {'granularity': timeframe})
        data = pd.DataFrame(data=info, columns=['Time', 'Low', 'High', 'Open', 'Close', 'Volume'])
        return data

