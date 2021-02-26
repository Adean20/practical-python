"""
Practical Python coursework
"""
# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(lines, select=None, types=None,
has_headers=True, delimiter=',', silence_errors=False):
    """
    Parse a CSV file into a list of records
    """
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")


    #with open(filename) as f_csv:
    rows = csv.reader(lines, delimiter=delimiter)

    if has_headers:
        headers = next(rows)
        #if a column selector was given find indices
        #and narrow headers
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select

    records = []
    for num, row in enumerate(rows, 1):
        #if empty line do nothing
        if not row:
            continue
        #filter the row if specific columns were selected
        if select:
            row = [row[index] for index in indices]

        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as err:
                if not silence_errors:
                    print(f"ValueError Line {num}: {row}")
                    print(f"{err}")
                continue

        #make the dictionary
        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
