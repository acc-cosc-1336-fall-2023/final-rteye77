#write functions here, don't add input('') statements here!
#write functions here, don't add input('') statements here!
class Stock:
    def __init__(self, symbol, company_name):
        self._symbol = symbol
        self._company_name = company_name

    def get_symbol(self):
        return self._symbol

    def get_company_name(self):
        return self._company_name

def stock_purchase_history():
    stock_apl = Stock('AAPL', 'Apple Inc')
    stock_cat = Stock('CAT', 'Caterpillar')
    stock_ek = Stock('EK', 'Eastman Kodak')
    stock_goog = Stock('GOOG', 'Google')
    stock_msft = Stock('MSFT', 'Microsoft')

    stock_dict = {
        'AAPL': stock_apl,
        'CAT': stock_cat,
        'EK': stock_ek,
        'GOOG': stock_goog,
        'MSFT': stock_msft
    }

    print("\nStock Purchase History:")
    for _, stock in stock_dict.items():
        print(f"{stock.get_company_name()} - {stock.get_symbol()}")