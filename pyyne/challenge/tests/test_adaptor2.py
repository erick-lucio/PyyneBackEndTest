import unittest
from datetime import datetime, timedelta
from pyyne.challenge.adapters.Bank2Adapter import Bank2Adapter

class TestBank2Adapter(unittest.TestCase):
    def setUp(self):
        self.bank2Adapter = Bank2Adapter()

    def test_get_balance_is_float(self):
        balance = self.bank2Adapter.get_balance()
        self.assertIsInstance(balance, float)

    def test_get_transactions_valid_result_contains_amount(self):
        from_date = datetime.now() - timedelta(days=30)
        to_date = datetime.now()
        transactions = self.bank2Adapter.get_transactions(12345, from_date, to_date)
        for transaction in transactions:
            self.assertIsInstance(transaction.get_text(),str)

    def test_get_transactions_valid_result_contains_valid_type_value(self):
        from_date = datetime.now() - timedelta(days=30)
        to_date = datetime.now()
        transactions = self.bank2Adapter.get_transactions(12345, from_date, to_date)
        for transaction in transactions:
         self.assertIsInstance(transaction.get_type().value, str)

    def test_get_transactions_valid_result_contains_valid_description_value(self):
        from_date = datetime.now() - timedelta(days=30)
        to_date = datetime.now()
        transactions = self.bank2Adapter.get_transactions(12345, from_date, to_date)
        for transaction in transactions:
            self.assertIsInstance(transaction.get_text(),str)