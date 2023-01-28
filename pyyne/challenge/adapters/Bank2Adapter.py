import datetime
import random
from bank2.integration.Bank2AccountBalance import Bank2AccountBalance
from bank2.integration.Bank2AccountSource import Bank2AccountSource

from bank2.integration.Bank2AccountBalance import Bank2AccountBalance

class Bank2Adapter:
    def __init__(self):
        self.bankBalance = Bank2AccountBalance(float(random.randint(0, 234387)), "USD")
        self.bankTransactions = Bank2AccountSource()

    def get_balance(self) -> float:
        return self.bankBalance.getBalance()

    def get_transactions(self, account_num:int, from_date:datetime.datetime, to_date:datetime.datetime):
        return self.bankTransactions.get_transactions (account_num, from_date, to_date)