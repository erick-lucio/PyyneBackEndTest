import unittest
import datetime
from pyyne.challenge.adapters.Bank2Adapter import Bank2Adapter

class TestBank2Adapter(unittest.TestCase):
    def setUp(self):
        self.bank2Adapter = Bank2Adapter()

    def test_get_balance_is_float(self):
        balance = self.bank2Adapter.get_balance()
        self.assertIsInstance(balance, float)

    def test_get_transactions_valid_result_contains_amount(self):
        from_date = datetime.datetime.now() - datetime.timedelta(days=30)
        to_date = datetime.datetime.now()
        transactions = self.bank2Adapter.get_transactions(12345, from_date, to_date)
        self.assertIn("qty:", transactions)

    def test_get_transactions_valid_result_contains_type(self):
        from_date = datetime.datetime.now() - datetime.timedelta(days=30)
        to_date = datetime.datetime.now()
        transactions = self.bank2Adapter.get_transactions(12345, from_date, to_date)
        self.assertIn("type:", transactions)

    def test_get_transactions_valid_result_contains_description(self):
        from_date = datetime.datetime.now() - datetime.timedelta(days=30)
        to_date = datetime.datetime.now()
        transactions = self.bank2Adapter.get_transactions(12345, from_date, to_date)
        self.assertIn("description:", transactions)

