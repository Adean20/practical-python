"""
TableFormatter helps create formatted reports
given headers and rows of data
"""
class TableFormatter:
    """
    Abstract base class used for
    formatting tables of data
    """
    def headings(self, headers):
        """
        Emit the table headings.
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        Emit a single row of table data.
        """
        raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    """
    Output portfolio data in Plain-Text format.
    """
    def headings(self, headers):
        for colname in headers:
            print(f'{colname:>10s}', end=" ")
        print()
        print(('-'*10 + " ")*len(headers))

    def row(self, rowdata):
        for data in rowdata:
            print(f'{str(data):>10s}', end=" ")
        print()

class CSVTableFormatter(TableFormatter):
    """
    Output portfolio data in CSV format.
    """
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    """
    Output portfolio data in HTML format.
    """
    def headings(self, headers):
        print("<tr><th>" + "</th><th>".join(headers) + "</th></tr>")

    def row(self, rowdata):
        print("<tr><td>" + "</td><td>".join(rowdata) + "</td></tr>")

class FormatError(Exception):
    """
    Raised when format type given to create_formatter is invalid
    """

def create_formatter(name):
    """
    Given 'txt', 'csv', or 'html'
    Return an appropriate formatter
    """
    options = {'txt': TextTableFormatter, 'csv': CSVTableFormatter,
    'html': HTMLTableFormatter}

    if name in options:
        return options.get(name)()

    raise FormatError(f"Unknown table format {name}")

def print_table(portfolio, columns, formatter):
    """
    Gets dict of stocks and prints a formatted table displaying
    only the columns given
    """
    formatter.headings(columns)

    rowdata = []
    for holding in portfolio:
        rowdata = [getattr(holding, attr) for attr in columns]
        formatter.row(rowdata)
