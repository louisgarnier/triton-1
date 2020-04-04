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
    # logger = logging.getLogger(__name__)
    logger.info("####### Started running #######")

    logger.info("Getting Quote for {}".format(args.quote))
    factory = ClientFactory()
    RESTAlpaca = factory.get_client('RESTAlpaca')

    AAPL = RESTAlpaca.getHistoricdata(args.quote)
    print(AAPL)
    AAPL = RESTAlpaca.getLastQuote(args.quote)
    print(AAPL)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser('Get quote for a stock.')
    parser.add_argument('-q', '--quote', help='Name of quote you want prices for', required=True)
    args = parser.parse_args()

    run(args)