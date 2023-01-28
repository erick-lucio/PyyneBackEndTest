import unittest
from datetime import datetime, timedelta
from pyyne.challenge.adapters.Bank1Adapter import Bank1Adapter

class TestBank1Adapter(unittest.TestCase):
    def setUp(self):
        self.bank1Adapter = Bank1Adapter()

    def test_get_balance(self):
        balance = self.bank1Adapter.get_balance(12345)
        self.assertIsInstance(balance, float)

    def test_get_transactions(self):
        from_date = datetime.now() - datetime.now() + timedelta(days=30)
        to_date = datetime.now()
        transactions = self.bank1Adapter.get_transactions(12345, from_date, to_date)
        self.assertIsInstance(transactions, str)
        self.assertIn("qty:", transactions)
        self.assertIn("type:", transactions)
        self.assertIn("description:", transactions)
        
    # def test_get_transactions_invalid_account(self):
    #     from_date = datetime.now() - datetime.now() + timedelta(days=30)
    #     to_date = datetime.now()
    #     with self.assertRaises(Exception):
    #         self.bank1Adapter.get_transactions(54321, from_date, to_date)
            
    # def test_get_transactions_invalid_dates(self):
    #     from_date = datetime.now() - timedelta(days=60)
    #     to_date = datetime.now() - datetime.now() + timedelta(days=30)
    #     with self.assertRaises(Exception):
    #         self.bank1Adapter.get_transactions(12345, from_date, to_date)           

        
    def test_get_transactions_valid_result_contains_type(self):
        from_date = datetime.now() - datetime.now() + timedelta(days=30)
        to_date = datetime.now()
        transactions = self.bank1Adapter.get_transactions(12345, from_date, to_date)
        self.assertIn("type:", transactions)

    def test_get_transactions_valid_result_contains_valid_amount_value(self):
        from_date = datetime.now() - datetime.now() + timedelta(days=30)
        to_date = datetime.now()
        transactions = self.bank1Adapter.get_transactions(12345, from_date, to_date)
        self.assertRegex(transactions, r'qty: \d+')      


    def test_get_transactions_valid_result_contains_valid_description_value(self):
        from_date = datetime.now() - datetime.now() + timedelta(days=30)
        to_date = datetime.now()
        transactions = self.bank1Adapter.get_transactions(12345, from_date, to_date)
        self.assertRegex(transactions, r'description: [A-Za-z]+')

    def test_get_transactions_valid_account_num(self):
        from_date = datetime.now() - datetime.now() + timedelta(days=30)
        to_date = datetime.now()
        transactions = self.bank1Adapter.get_transactions(12345, from_date, to_date)
        self.assertIsNotNone(transactions)

    def test_get_transactions_valid_result_contains_amount(self):
        from_date = datetime.now() - datetime.now() + timedelta(days=30)
        to_date = datetime.now()
        transactions = self.bank1Adapter.get_transactions(12345, from_date, to_date)
        self.assertIn("qty:", transactions)       

        
    def test_get_transactions_valid_result_contains_description(self):
        from_date = datetime.now() - datetime.now() + timedelta(days=30)
        to_date = datetime.now()
        transactions = self.bank1Adapter.get_transactions(12345, from_date, to_date)
        self.assertIn("description:", transactions)
        
    def test_get_transactions_with_valid_account_number(self):
        from_date = datetime.now() - datetime.now() + timedelta(days=30)
        to_date = datetime.now()
        transactions = self.bank1Adapter.get_transactions(12345, from_date, to_date)
        self.assertIsNotNone(transactions)      

        
    # def test_get_transactions_with_valid_date_range(self):
    #     from_date = datetime.now() - datetime.now() + timedelta(days=30)
    #     to_date = datetime.now()
    #     transactions = self.bank1Adapter.get_transactions(12345, from_date, to_date)
    #     self.assertIsNotNone(transactions)        

