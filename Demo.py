#!/usr/bin/env python3

import datetime
import json
import logging
import os
import sys

from ClientFactory import ClientFactory
import Utils

logger = logging.getLogger(__name__)
logging_map = {'DEBUG': logging.DEBUG,
               'INFO': logging.INFO,
               'WARNING': logging.WARNING,
               'ERROR': logging.ERROR}

def run(args):
    # Logging
    date = datetime.datetime.now()
    log_directory = date.strftime('logs/{}'.format(__file__))
    Utils.CreateDirectory(log_directory)
    log_file_name = date.strftime('%d_%m_%Y_%H.log')
    logging.basicConfig(filename=("{}/{}".format(log_directory, log_file_name)), level=logging.INFO)
    logger.info("####### Started running #######")

    logger.info("Getting Quote for {}".format(args.quote))
    factory = ClientFactory()
    RESTAlpaca = factory.get_client('RESTAlpaca')
    RESTAlpaca.setAccount("Paper")

    accountInfo = RESTAlpaca.getAccountInfo()
    print(accountInfo)

    assetInfo = RESTAlpaca.getAssetInfo(args.quote)
    print(assetInfo)

    stockQuote = RESTAlpaca.getLastQuote(args.quote)
    print(stockQuote)

    stockHistoricalData = RESTAlpaca.getHistoricdata(args.quote, multiplier=1, timespan='day', _from="2020-01-01", to="2020-03-15")
    print(stockHistoricalData)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser('Get quote for a stock.')
    parser.add_argument('-t', '--ticker', help='Name of ticker you want prices for', required=True)
    args = parser.parse_args()

    run(args)