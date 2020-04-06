import datetime
import json
import logging
import requests

import alpaca_trade_api as tradeapi
from clients.AbstractClient import AbstractClient

# Using alpaca_trade_api package: https://github.com/alpacahq/alpaca-trade-api-python

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
        self.logger.info("This endpoit uses polygon service, therefore might not work if you only have an Alpaca Paper account.")
        return self.api.polygon.last_quote(symbol)

    def getHistoricQuotesPolygon(self, symbol, multiplier, timespan, _from, to, unadjusted=False, limit=None):
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
        self.logger.info("This endpoit uses polygon service, therefore might not work if you only have an Alpaca Paper account.")
        return self.api.polygon.historic_agg_v2(symbol, 1, 'day', _from=_from, to=to, unadjusted=unadjusted, limit=limit).df

    def getHistoricQuotesAV(self, symbol, adjusted=False, outputsize='full', cadence='daily', output_format=None):
        """
        Returns a csv, json, or pandas object of historical OHLCV data.
        """
        return self.api.alpha_vantage.historic_quotes(symbol, adjusted=adjusted, outputsize=outputsize, cadence=cadence, output_format=output_format)

    def getLastQuoteAV(self, symbol):
        """
        Returns a json object with the current OHLCV data of the selected symbol (same as current_quote).
        """
        self.logger.info("getLastQuoteAV({})".format(symbol))
        return self.api.alpha_vantage.last_quote(symbol)

    def getCurrentQuoteAV(self, symbol):
        """
        Returns a json object with the current OHLCV data of the selected symbol (same as current_quote).
        """
        self.logger.info("getCurrentQuoteAV({})".format(symbol))
        return self.api.alpha_vantage.current_quote(symbol)
