
The [jsonrates](http://jsonrates.com) API provides reliable, fast and free exchange rates and currency conversion for 168 currencies. All exchange rates are updated every 10 minutes and were collected from several providers. Historical rates are provided from 2002, for Bitcoin from 2010.

[jsonrates – Currency exchange rates JSON API](http://jsonrates.com)

The above script requires `requests`

#### To install requests

```shell
$ apt-get install python-pip
$ pip install requests
```

Tested on

* Debian 7.8 (wheezy) with Python 2.7.3
* Mac OS X Yosemite 10.10.2 with Python 2.7.6

The jsonRatesXBT.py retrieves current [Bitcoin](https://bitcoin.org/en/) rates in various currencies.
