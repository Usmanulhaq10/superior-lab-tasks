from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.update_balance(self.get_balance() + interest)
        return f"Interest applied. New Balance: {self.get_balance()}"

    def withdraw(self, amount):
        if 0 < amount <= self.get_balance():
            self.update_balance(self.get_balance() - amount)
            return f"Withdrew {amount}. Remaining Balance: {self.get_balance()}"
        return "Insufficient funds or invalid withdrawal amount."