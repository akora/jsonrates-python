#!/usr/bin/python

# The jsonrates API provides reliable, fast and free exchange rates and currency conversion for 168 currencies.
# All exchange rates are updated every 10 minutes and were collected from several providers.
# Historical rates are provided from 2002, for Bitcoin from 2010.

import sys
import requests

base_url = 'http://jsonrates.com/get/'
from_currency = 'XBT'
rates_in = ['GBP', 'USD', 'EUR', 'HUF']


def get_currency_rate(from_currency, rate_currency):
  query = base_url + '?from=%s&to=%s' % (from_currency, rate_currency)
  try:
    response = requests.get(query)
    # print("[%s] %s" % (response.status_code, response.url))
    if response.status_code != 200:
      response = 'N/A'
      return response
    else:
      rates = response.json()
      rate_in_currency = float(rates['rate'])
      return rate_in_currency
  except requests.ConnectionError as error:
    print error
    sys.exit(1)


def main():
  for rate_currency in rates_in:
    rate = get_currency_rate(from_currency, rate_currency)
    print rate_currency, ("%.2f" % rate)

if __name__ == '__main__':
  main()

# TODO: fix KeyError: 'rate' issue if from_currency or rates_in is malformed
