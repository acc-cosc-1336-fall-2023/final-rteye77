#write functions here, don't add input('') statements here!
class Stock:
    def __init__(self, symbol, company_name):
        self._symbol = symbol
        self._company_name = company_name

    def get_symbol(self):
        return self._symbol

    def get_company_name(self):
        return self._company_name


def get_stock_list():
    stocks = {}
    try:
        with open('stocklist.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split()
                symbol = data[0]
                company_name = ' '.join(data[1:])
                stocks[symbol] = Stock(symbol, company_name)
    except FileNotFoundError:
        print("File not found or unable to open.")
    return stocks


def display_stock_list(stock_dict):
    for _, stock in stock_dict.items():
        print(f"{stock.get_company_name()} - {stock.get_symbol()}")


def test_config():
    return True