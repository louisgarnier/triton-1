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

    def setAccount(self, accountType):
        self.accountType = accountType
        if self.accountType == "Live":
            self.api = tradeapi.REST(key_id=self.cfg_file['Live']['api_key'],
                                     secret_key=self.cfg_file['Live']['secret_key'],
                                     base_url=self.cfg_file['Live']['base_route'],
                                     api_version='v2')
        elif self.accountType == "Paper":
            self.api = tradeapi.REST(key_id=self.cfg_file['Paper']['api_key'],
                                     secret_key=self.cfg_file['Paper']['secret_key'],
                                     base_url=self.cfg_file['Paper']['base_route'],
                                     api_version='v2')

    def getAccountInfo(self):
        return self.api.get_account()

    def getAssetInfo(self, symbol):
        return self.api.get_asset(symbol)

    def getLastQuote(self, symbol):
        return self.api.polygon.last_quote(symbol)

    def getHistoricdata(self, symbol, multiplier, timespan, _from, to, unadjusted=False, limit=None):
        """
        multiplier: integer affecting the amount of data contained in each Agg object.
        timespan:   string affecting the length of time represented by each Agg object.
                    It is one of the following values: minute, hour, day, week, month, quarter, year
        _from:      Eastern Time timestamp string that filters the result for the lower bound, inclusive.
        to:         is an Eastern Time timestamp string that filters the result for the upper bound, inclusive.
        unadjusted: can be set to true if results should not be adjusted for splits.
        limit:      integer to limit the number of results. 3000 is the default and max value.

        Outputs data is a pandas DF
        """
        return self.api.polygon.historic_agg_v2(symbol, 1, 'day', _from=_from, to=to, unadjusted=unadjusted, limit=limit).df
