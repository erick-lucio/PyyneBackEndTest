
from pyyne.challenge.bank.BankController import BankController


if __name__ == "__main__":
    bank_controller = BankController()
    bank_controller.print_balances(123)
    bank_controller.print_transactions(123, "2019-01-01", "2019-01-31")