
from . import fileparse
from . import stock

class Portfolio:
    """
    Class to hold instances of Stock classes
    """
    def __init__(self):
        self._holdings = []

    @classmethod
    def from_csv(cls, lines, **opts):
        self = cls()
        portdicts = fileparse.parse_csv(lines, select=['name', 'shares', 'price'],
        types=[str,int,float], **opts)

        for d in portdicts:
            self.append(stock.Stock(**d))

        return self

    def append(self, holding):
            if not isinstance(holding, stock.Stock):
                raise TypeError("Expected a Stock instance")
            self._holdings.append(holding)

    def __iter__(self):
        return self._holdings.__iter__()

    def __len__(self):
        return len(self._holdings)

    def __getitem__(self, index):
        return self._holdings[index]

    def __contains__(self, name):
        return any(stock.name == name for stock in self._holdings)

    
    @property
    def total_cost(self):
        """
        Returns total value of portfolio
        """
        return sum(stock.cost for stock in self._holdings)

    def tabulate_shares(self):
        """
        Calculates total shares for each stock
        """
        from collections import Counter
        total_shares = Counter()
        for stock in self._holdings:
            total_shares[stock.name] += stock.shares
        return total_shares
