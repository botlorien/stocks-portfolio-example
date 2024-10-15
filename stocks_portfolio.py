
class StocksPortfolio:
    _stocks:dict

    def __init__(self,stocks:dict={}) -> None:
        self.stocks = stocks

    @property
    def stocks(self):
        return self._stocks
    
    @stocks.setter
    def stocks(self,new):
        if isinstance(new,dict):
            self._stocks=new
        else:
            raise ValueError(
                "Stocks value needs to be instance of dict class"
            )

    def __add__(self,other):
        if isinstance(other,StocksPortfolio):
            combined_stocks = self.stocks.copy()
            for stock in other.stocks:
                if stock in combined_stocks:
                    combined_stocks[stock] += other.stocks[stock]
                else:
                    combined_stocks[stock] = other.stocks[stock]
            return StocksPortfolio(combined_stocks)
        else:
            raise ValueError(
                "Adition object needs to be instance of StockPortfolio"
            )
            

    def __mul__(self,scalar):
        if isinstance(scalar,(int,float)):
            mul_stocks = self.stocks.copy()
            for stock in mul_stocks:
                mul_stocks[stock] *= scalar
            return StocksPortfolio(mul_stocks)
        else:
            raise ValueError(
                "The scalar value needs to be integer or float"
            )

    def __getitem__(self,stock):
        return self.stocks.get(stock,0)

    def __len__(self):
        return len(self.stocks)

    def __abs__(self):
        return sum(list(self.stocks.values()))

    def __repr__(self) -> str:
        return f'StocksPortfolio({self.stocks!r})'

    def __bool__(self):
        return any(value > 0 for value in self.stocks.values())

if __name__=='__main__':
    portfolio1 = StocksPortfolio({
        'ASDF':10,
        'GHJL':5
    })
    portfolio2 = StocksPortfolio({
        'ASDF':10,
        'ZXCV':5,
    })
    portfolio3=StocksPortfolio()

    combined_portfolio = portfolio1 + portfolio2
    mul_portfolio = portfolio1 * 3
    print('combined_portfolio: ',combined_portfolio)
    print('mul_portfolio: ',mul_portfolio)
    print('portfolio1: ',portfolio1)
    print('portfolio2: ',portfolio2)
    print('len: ',len(portfolio1))
    print('abs: ',abs(portfolio1))
    print('bool: ',bool(portfolio1),bool(portfolio3))
    print('portfolio1["ASDF"]: ',portfolio1['ASDF'])