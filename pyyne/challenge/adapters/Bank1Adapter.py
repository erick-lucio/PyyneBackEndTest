import datetime
from bank1.integration.Bank1AccountSource import Bank1AccountSource
from bank2.integration.Bank2AccountBalance import Bank2AccountBalance


class Bank1Adapter:
    def __init__(self):
        self.bankAccounts = Bank1AccountSource()

    def get_balance(self, account_num:int) -> float:
        return self.bankAccounts.get_account_balance(account_num)

    def get_transactions(self, account_num:int, from_date:datetime.datetime, to_date:datetime.datetime):     
        return self.bankAccounts.get_transactions(account_num, from_date, to_date)

