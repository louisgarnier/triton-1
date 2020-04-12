#!/usr/bin/env python3

import datetime
import json
import logging
import os
import sys

from ClientFactory import ClientFactory
import Utils

logging_map = {'DEBUG': logging.DEBUG,
               'INFO': logging.INFO,
               'WARNING': logging.WARNING,
               'ERROR': logging.ERROR}

def run(args):
    # Logging
    log_directory = 'logs/{}'.format(__file__)
    log_file_name = datetime.datetime.now().strftime('%d_%m_%Y_%H.log')
    Utils.CreateDirectory(log_directory)

    logger = logging.getLogger(__name__)
    # logging.basicConfig(filename=("{}/{}".format(log_directory, log_file_name)), level=logging_map['DEBUG'])
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging_map['DEBUG'])

    logger.info("####### Running {}:{} #######".format(__file__, __name__))
    logger.info("Getting Quote for {}".format(args.ticker))

    factory = ClientFactory()
    RESTAlpaca = factory.get_client('RESTAlpaca')
    RESTAlpaca.setAccount("Paper")
    RESTCryptocompare = factory.get_client('RESTCryptocompare')
    RESTCoinbase = factory.get_client('RESTCoinbase')

    # ALPACA CALLS
    # accountInfo = RESTAlpaca.getAccountInfo()
    # print(accountInfo)
    # assetInfo = RESTAlpaca.getAssetInfo(args.ticker)
    # print(assetInfo)
    # stockQuote = RESTAlpaca.getLastQuote(args.ticker)
    # print(stockQuote)
    # stockHistoricalData = RESTAlpaca.getHistoricQuotesAV(args.ticker, adjusted=True, output_format='pandas')
    # print(stockHistoricalData)
    # stockCurrentQuoteAV = RESTAlpaca.getCurrentQuoteAV(args.ticker)
    # print(stockCurrentQuoteAV)
    stockLastQuoteAV = RESTAlpaca.getLastQuoteAV(args.ticker)
    print(stockLastQuoteAV)

    # CRYPTOCOMPARE CALLS
    price = RESTCryptocompare.getPrice('BTC')
    print(price)
    # histo = RESTCryptocompare.getBlockchainHisto(args.ticker)
    # print(histo)

    # COINBASE CALLS
    # accounts = RESTCoinbase.listAccounts()
    # print(accounts)
    # orders = RESTCoinbase.listOrders()
    # print(orders)
    # products = RESTCoinbase.getProducts()
    # print(products)
    # book = RESTCoinbase.getBook('ETH-USD')
    # print(book)
    ticker = RESTCoinbase.getBook('ETH-USD')
    print(ticker)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser('Get quote for a stock.')
    parser.add_argument('-t', '--ticker', help='Name of ticker you want prices for', required=True)
    args = parser.parse_args()

    run(args)