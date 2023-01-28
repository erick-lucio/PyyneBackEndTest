import datetime

class Bank1AccountSource:

    def get_account_balance(self, account_id):
        return 215.5

    def get_account_currency(self, account_id):
        return "USD"

    def get_transactions(self, account_id, from_date, to_date):
        return [
            {"amount": 100.0, "type": "credit", "description": "Check deposit"},
            {"amount": 25.5, "type": "debit", "description": "Debit card purchase"},
            {"amount": 225.0, "type": "debit", "description": "Rent payment"}
        ]
