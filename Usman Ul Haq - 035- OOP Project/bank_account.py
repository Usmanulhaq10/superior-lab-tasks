class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.__account_number = account_number  
        self.__account_holder = account_holder
        self.__balance = balance

    def get_account_details(self):
        return {
            "Account Number": self.__account_number,
            "Account Holder": self.__account_holder,
            "Balance": self.__balance,
        }

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New Balance: {self.__balance}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        raise NotImplementedError("Withdraw method must be implemented by subclasses.")

    def get_balance(self):
        return self.__balance

    def update_balance(self, new_balance):
        self.__balance = new_balance
