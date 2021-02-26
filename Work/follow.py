"""
Script that reads portfolio like a stock ticker
"""
import os
import time

def follow(filename):
    """
    Generator that produces a line from end of a file
    """

    file = open(filename)
    file.seek(0, os.SEEK_END)
    while True:
        line = file.readline()
        if line == "":
            time.sleep(0.1)
            continue
        yield line


if __name__ == '__main__':
    import report

    portfolio = report.read_portfolio('Data/portfolio.csv')

    for data in follow('Data/stocklog.csv'):
        fields = data.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
