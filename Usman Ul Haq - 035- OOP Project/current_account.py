from bank_account import BankAccount

class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.get_balance() + self.overdraft_limit:
            self.update_balance(self.get_balance() - amount)
            return f"Withdrew {amount}. Remaining Balance: {self.get_balance()}"
        return "Withdrawal exceeds overdraft limit."
