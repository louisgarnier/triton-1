import datetime
import json
import logging
import pandas as pd
import requests
import sys

import alpaca_trade_api as tradeapi
from clients.AbstractClient import AbstractClient

# https://min-api.cryptocompare.com/documentation

class RESTCryptocompare(AbstractClient):
    def __init__(self):
        super(RESTCryptocompare, self).__init__()
        self.logger = logging.getLogger(__name__)
        self.logger.info("Initiating Cryptocompare client")
        self.load_config("Cryptocompare")

    def getPrice(self, ticker):
        url = "https://min-api.cryptocompare.com/data/price?fsym={ticker}&tsyms=EUR,USD,GBP,EUR".format(ticker=ticker)
        response = self._get(url)
        return response


    def getBlockchainHisto(self, symbol, limit=2000):
        """
            Returns a Pandas DataFrame
        """
        url = 'https://min-api.cryptocompare.com/data/blockchain/histo/day?api_key={api_key}&limit={limit}&fsym={symbol}'.format(api_key=self.cfg_file['api_key'], limit=limit, symbol=symbol)
        response = self._get(url)
        try:
            data = response["Data"]["Data"]
        except KeyError:
            sys.exit("No Data returned for this ticker")
        df = pd.DataFrame(data)
        return df