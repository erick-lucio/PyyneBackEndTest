import datetime

from bank2.integration.Bank2AccountBalance import Bank2AccountBalance
from bank2.integration.Bank2AccountTransaction import Bank2AccountTransaction

class Bank2AccountSource:
    def get_balance(self, account_num:int) -> Bank2AccountBalance:
        return Bank2AccountBalance(512.5, "USD")

    def get_transactions(self, account_num:int, from_date:datetime.datetime, to_date:datetime.datetime):
        return [
            Bank2AccountTransaction(125, Bank2AccountTransaction.TRANSACTION_TYPES.DEBIT, "Amazon.com"),
            Bank2AccountTransaction(500, Bank2AccountTransaction.TRANSACTION_TYPES.DEBIT, "Car insurance"),
            Bank2AccountTransaction(800, Bank2AccountTransaction.TRANSACTION_TYPES.CREDIT, "Salary")
        ]
