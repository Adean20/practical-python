#!/usr/bin/env python3
"""
Practical Python Coursework
"""
# report.py
#
# Exercise 2.4

import sys
import fileparse
import tableformat
from stock import Stock
from portfolio import Portfolio

def read_portfolio(filename, **opts):
    """
    Takes csv file containing 'name', 'shares', 'price' columns.
    Returns a portfolio object
    """
    with open(filename) as file:
        portfolio_dict = fileparse.parse_csv(file, select=['name', 
        'shares', 'price'], types=[str, int, float], **opts)

        portfolio = [Stock(**holding) for holding in portfolio_dict]

        return Portfolio(portfolio)


def read_prices(filename):
    """
    Takes CSV file with Symbol, Prices
    Returns Dictionary
    """
    with open(filename) as file:
        return dict(fileparse.parse_csv(file,
        types=[str, float], has_headers=False))


def make_report_data(portfolio, prices):
    """
    Creates a list of (name, shares, price, change) tuples
    from portfolio and price dicts
    """
    report_list = []

    for holding in portfolio:
        current_value = prices[holding.name]
        change = current_value - holding.price
        report_list.append((holding.name, holding.shares, current_value, change))

    return report_list

def print_report(report_list, formatter, fmt='txt'):
    """
    Prints a formatted report
    from list provided by make_report_data
    """
    formatter.headings(["Ticker", "Shares", "Price", "Change"])

    if fmt == 'txt':
        currency = "$"
    else:
        currency = ""

    for name, shares, price, change in report_list:
        rowdata = [name, str(shares), f'{currency}{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    """
    Reads two csv files(Portfolio, Prices) and generates a report.
    """
    portfolio = read_portfolio(portfolio_filename)
    current_values = read_prices(prices_filename)

    report = make_report_data(portfolio, current_values)

    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter, fmt)

def main(args):
    """
    Generate and print report
    """
    portfolio_file = args[1]
    price_file = args[2]
    portfolio_report(portfolio_file, price_file)

if __name__ == "__main__":

    if len(sys.argv) != 3:
        raise SystemExit(f'Usage: {sys.argv[0]} portfolio_file price_file')

    main(sys.argv)
