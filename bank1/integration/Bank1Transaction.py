class Bank1Transaction:
    TYPE_CREDIT = 1
    TYPE_DEBIT = 2

    def __init__(self, amount, type, text):
        self.amount = amount
        self.type = type
        self.text = text

    def get_amount(self):
        return self.amount

    def get_type(self):
        return self.type

    def get_text(self):
        return self.text
