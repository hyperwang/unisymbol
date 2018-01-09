from symbols import SYMBOL_DICTS, SUPPORTED_SYMBOLS


__all__ = []

def SymbolFactory(asset1, asset2):
    def __init__(self, exchange=None):
        self.exchange = exchange
        super(self.__class__, self).__init__()

    def __str__(self):
        if self.exchange is None:
            return self.__class__.__name__
        return self.symbol_dict[self.exchange]
            
    sym_tuple = (asset1, asset2)
    sym_str = "{}_{}".format(*sym_tuple).upper()
    _sym_dict = {}
    for exch, sdict in SYMBOL_DICTS.iteritems():
        s = sdict.get(sym_tuple)
        if s is None:
            continue
        _sym_dict[exch] = s
    attributes = {'symbol_dict': _sym_dict, '__init__': __init__, '__str__': __str__}
    new_class = type(sym_str, (str,), attributes)
    globals()[sym_str] = new_class
    __all__.append(sym_str)
    return new_class


for ssb in SUPPORTED_SYMBOLS:
    SymbolFactory(*ssb)
