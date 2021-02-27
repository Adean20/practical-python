#!/usr/bin/env python3
"""
Practical Python Coursework
"""
# pcost.py
#
# Exercise 1.27
import sys
from .report import read_portfolio

def portfolio_cost(filename):
    """
    Takes csv file containing 'shares' and 'price' columns.
    Prints cost of portfolio.
    """

    holdings = read_portfolio(filename)
    return holdings.total_cost

def main(args):
    """
    Reads portfolio file and prints total cost of portfolio
    """
    portfolio_file = args[1]
    cost = portfolio_cost(portfolio_file)
    print("Total cost:", round(cost, 2))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f'Usage: {sys.argv[0]} portfolio_file')

    main(sys.argv)
