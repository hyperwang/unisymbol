import itertools


SYMBOL_DICTS = {
    'okex': {
        ('BCH', 'BTC'): 'bch_btc',
    },
    'bitfinex': {
        ('BCH', 'BTC'): 'bchbtc',
    },
}

SUPPORTED_SYMBOLS = list(itertools.chain.from_iterable([sd.keys() for sd in SYMBOL_DICTS.values()]))
