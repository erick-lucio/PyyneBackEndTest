from pyyne.challenge.adapters.Bank1Adapter import Bank1Adapter
from pyyne.challenge.adapters.Bank2Adapter import Bank2Adapter


class BankController:
    def __init__(self):
        self.bank1_adapter = Bank1Adapter()
        self.bank2_adapter = Bank2Adapter()

    def print_balances(self, accountId):
        balance1 = self.bank1_adapter.get_balance(accountId)
        print("Balance for bank1 account {}".format(accountId), balance1)
        balance2 = self.bank2_adapter.get_balance()
        print("Balance for bank2 account {}".format(accountId), balance2)
        print("\n")

    def print_transactions(self, accountId, from_date, to_date):
        transactions1 = self.bank1_adapter.get_transactions(accountId, from_date, to_date)
        print("Transactions for bank1 account {}: between {}: and {}:".format(accountId, from_date, to_date), transactions1)
        transactions2 = self.bank2_adapter.get_transactions(accountId, from_date, to_date)
        print("Transactions for bank2 account {}: between {}: and {}:".format(accountId, from_date, to_date), transactions2)

