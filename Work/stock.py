"""
Practical Python Coursework
"""
from typedproperty import typedproperty

class Stock:
    """
    Contains name, shares,
    price of a stock in a portfolio
    """
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        """
        Value of shares * price
        """
        return self.shares * self.price

    def sell(self, numshares):
        """
        Removes shares from instance
        """
        self.shares -= numshares

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"
