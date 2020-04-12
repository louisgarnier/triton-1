import base64
import datetime
import hashlib
import hmac
import json
import logging
import requests
import time

from clients.AbstractClient import AbstractClient

# Using Documentation: https://docs.pro.coinbase.com/#introduction

"""
    Creating a Request
    All REST requests must contain the following headers:

    CB-ACCESS-KEY The api key as a string.
    CB-ACCESS-SIGN The base64-encoded signature (see Signing a Message).
    CB-ACCESS-TIMESTAMP A timestamp for your request.
    CB-ACCESS-PASSPHRASE The passphrase you specified when creating the API key.
    All request bodies should have content type application/json and be valid JSON.
"""

class RESTCoinbase(AbstractClient):
    def __init__(self):
        super(RESTCoinbase, self).__init__()
        self.logger = logging.getLogger(__name__)
        self.logger.info("Initiating Coinbase client")
        self.load_config("Coinbase")
        self.auth = None
        self.session = requests.Session()

    def getHeaders(self, method, request_path, body=None):
        timestamp = str(time.time())
        hmac_key = base64.b64decode(self.cfg_file['secret_key'])
        message = "{timestamp}{method}{request_path}"
        if body:
            message = "{timestamp}{method}{request_path}{body}"
        message = message.format(timestamp=timestamp,
                                 method=method.upper(),
                                 request_path=request_path,
                                 body=body)
        message = message.encode('ascii')
        signature = hmac.new(hmac_key, message, hashlib.sha256)
        signature_b64 = base64.b64encode(signature.digest()).decode('utf-8')
        return {
            'Content-Type': 'Application/JSON',
            'CB-ACCESS-SIGN': signature_b64,
            'CB-ACCESS-TIMESTAMP': timestamp,
            'CB-ACCESS-KEY': self.cfg_file['api_key'],
            'CB-ACCESS-PASSPHRASE': self.cfg_file['passphrase']
        }

    def listAccounts(self):
        url = "{}{}".format(self.cfg_file['api_url'], '/accounts')
        data = self._get(url, self.getHeaders('get', '/accounts'))
        return data

    def listOrders(self):
        url = "{}{}".format(self.cfg_file['api_url'], '/orders')
        data = self._get(url, self.getHeaders('get', '/orders'))
        return data

    def getProducts(self):
        url = "{}{}".format(self.cfg_file['api_url'], '/products')
        data = self._get(url, self.getHeaders('get', '/products'))
        return data

    def getBook(self, product_id):
        """
            get back: {
                "sequence": "3",
                "bids": [
                    [ price, size, num-orders ],
                ],
                "asks": [
                    [ price, size, num-orders ],
                ]
            }
        """
        url = "{}{}".format(self.cfg_file['api_url'], '/products/{}/book'.format(product_id))
        data = self._get(url, self.getHeaders('get', '/products/{}/book'.format(product_id)))
        return data

    def getTicker(self, product_id):
        data = self.send_message('get', '/products/{}/ticker'.format(product_id))
        return data

