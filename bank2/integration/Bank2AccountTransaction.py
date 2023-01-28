from enum import Enum

class Bank2AccountTransaction:
    class TRANSACTION_TYPES(Enum):
        DEBIT = "DEBIT"
        CREDIT = "CREDIT"
    def __init__(self, amount:float, type:TRANSACTION_TYPES, text:str):
        self.amount = amount
        self.type = type
        self.text = text

    def get_amount(self):
        return self.amount

    def get_type(self):
        return self.type

    def get_text(self):
        return self.text
