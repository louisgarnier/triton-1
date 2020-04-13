import logging
import datetime
from clients.Alpaca import RESTAlpaca
from clients.Cryptocompare import RESTCryptocompare
from clients.Coinbase import RESTCoinbase

class ClientFactory(object):
    def __init__(self):
        self.clients = {}
        self.logger = logging.getLogger(__name__)
        self.logger.info("initiating the clients factory")
        self.clients["RESTAlpaca"] = RESTAlpaca()
        self.clients["RESTCryptocompare"] = RESTCryptocompare()
        self.clients["RESTCoinbase"] = RESTCoinbase()

    def get_client(self, name):
        if name == "" or name is None:
            raise ValueError("Client name cannot be null or empty")
        if name in self.clients:
            return self.clients[name]
        else:
            raise ValueError("No client found: " + name)
