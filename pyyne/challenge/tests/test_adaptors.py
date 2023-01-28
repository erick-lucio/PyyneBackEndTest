import unittest
import datetime


from pyyne.challenge.adapters.Bank1Adapter import Bank1Adapter
from pyyne.challenge.adapters.Bank2Adapter import Bank2Adapter
from bank2.integration.Bank2AccountBalance import Bank2AccountBalance

class TestBank1Adapter(unittest.TestCase):
    def setUp(self):
        self.bank1Adapter = Bank1Adapter()

    def test_get_balance(self):
        balance = self.bank1Adapter.get_balance(12345)
        self.assertIsInstance(balance, float)

    def test_get_transactions(self):
        from_date = datetime.datetime.now() - datetime.timedelta(days=30)
        to_date = datetime.datetime.now()
        transactions = self.bank1Adapter.get_transactions(12345, from_date, to_date)
        self.assertIsInstance(transactions, str)
        self.assertIn("qty:", transactions)
        self.assertIn("type:", transactions)
        self.assertIn("description:", transactions)

class TestBank2Adapter(unittest.TestCase):
    def setUp(self):
        self.bank2Adapter = Bank2Adapter()

    def test_get_balance(self):
        balance = self.bank2Adapter.get_balance()
        self.assertIsInstance(balance, float)

    def test_get_transactions(self):
        from_date = datetime.datetime.now() - datetime.timedelta(days=30)
        to_date = datetime.datetime.now()
        transactions = self.bank2Adapter.get_transactions(12345, from_date, to_date)
        self.assertIsInstance(transactions, str)
        self.assertIn("qty:", transactions)
        self.assertIn("type:", transactions)
        self.assertIn("description:", transactions)

