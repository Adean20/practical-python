"""
Reads a portfolio file and log file
Displays a running table of name, price, change
for each stock in portfolio file that is updated
in the log file
"""
import sys
import csv
from . import report
from . import tableformat
from .follow import follow

def select_columns(rows, indices):
    """
    Selects which columns to use
    """
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    """
    Converts data in rows to specified type list
    """
    for row in rows:
        yield [cast(item) for cast, item in zip(types, row)]

def make_dicts(rows, headers):
    """
    Creates a dictionary based on data with headers being keys
    """
    for row in rows:
        yield dict(zip(headers, row))

def parse_stock_data(lines):
    """
    Utilizes above methods to parse data from given csv lines
    """
    rows = csv.reader(lines)
    rows = select_columns(rows, [0,1,4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, headers=['name', 'price', 'change'])
    return rows

def filter_symbols(rows, names):
    """
    Filters out any stock not in portfolio
    """
    for row in rows:
        if row['name'] in names:
            yield row

def ticker(portfolio_file, log_file, fmt):
    """
    Reads a portfolio file and log file
    Displays a running table of name, price, change
    for each stock in portfolio file that is updated
    in the log file
    """
    portfolio = report.read_portfolio(portfolio_file)
    rows = parse_stock_data(follow(log_file))
    rows = (row for row in rows if row['name' in portfolio])

    formatter = tableformat.create_formatter(fmt)
    formatter.headings(["Name", "Price", "Change"])
    for row in rows:
        formatter.row([row['name'], row['price'], row['change']])

def main(args):
    """
    Calls ticker function from supplied arguments on commandline
    """
    if len(args) != 4:
        raise SystemExit(f"Usage: {args[0]} portfolio_file log_file fmt")
    ticker(args[1], args[2], args[3])

if __name__ == '__main__':
    main(sys.argv)
