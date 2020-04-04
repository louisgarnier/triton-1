import datetime
import json
import logging
import requests

import alpaca_trade_api as tradeapi
from clients.AbstractClient import AbstractClient

class RESTAlpaca(AbstractClient):
    def __init__(self):
        super(RESTAlpaca, self).__init__()
        self.logger = logging.getLogger(__name__)
        self.logger.info("Initiating Alpaca client")
        self.load_config("Alpaca")
        self.api = tradeapi.REST(self.cfg_file['Account']['api_key'],
                                 self.cfg_file['Account']['secret_key'],
                                 api_version='v2')

    def getAccountInfo(self):
        return self.api.get_account()

    def getAsset(self, symbol):
        return self.api.get_asset(symbol)

    def getLastQuote(self, symbol):
        return self.api.polygon.last_quote(symbol)

    def getHistoricdata(self, symbol):
        return self.api.polygon.historic_agg_v2(symbol, 1, 'day', _from='2019-01-01', to='2019-02-01').df
