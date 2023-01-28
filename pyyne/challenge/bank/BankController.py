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
        transactions1Content = ""   
        for item in transactions1:
            transactions1Content += "\nqty: {}, type: {}, description: {}".format(item['amount'], item['type'], item['description'])
        transactions1Content += "\n"
        print("Transactions for bank1 account {}: between {}: and {}:".format(accountId, from_date, to_date), transactions1Content)

        transactions2 = self.bank2_adapter.get_transactions(accountId, from_date, to_date)
        transactions2Content = ""   
        for item in transactions2:
            transactions2Content += "\nqty: {}, type: {}, description: {}".format(item.get_amount(), item.get_type().value, item.get_text())
        transactions2Content += "\n"

        print("Transactions for bank2 account {}: between {}: and {}:".format(accountId, from_date, to_date), transactions2Content)
