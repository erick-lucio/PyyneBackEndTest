class Bank2AccountBalance:
    def __init__(self, balance:float, currency:str):
        self.balance = balance
        self.currency = currency

    def getBalance(self):
        return self.balance

    def getCurrency(self):
        return self.currency
