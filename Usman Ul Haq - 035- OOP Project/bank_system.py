import csv
from savings_account import SavingsAccount
from current_account import CurrentAccount

class BankSystem:
    def __init__(self, filename="accounts.csv"):
        self.accounts = []
        self.filename = filename
        self.load_accounts()

    def load_accounts(self):
        try:
            with open(self.filename, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["Type"] == "Savings":
                        account = SavingsAccount(
                            row["Account Number"],
                            row["Account Holder"],
                            float(row["Balance"]),
                            float(row["Interest Rate"]),
                        )
                    elif row["Type"] == "Current":
                        account = CurrentAccount(
                            row["Account Number"],
                            row["Account Holder"],
                            float(row["Balance"]),
                            float(row["Overdraft Limit"]),
                        )
                    self.accounts.append(account)
        except FileNotFoundError:
            print("No previous account data found. Starting fresh.")

    def save_accounts(self):
        with open(self.filename, "w", newline="") as file:
            fieldnames = [
                "Account Number",
                "Account Holder",
                "Balance",
                "Type",
                "Interest Rate",
                "Overdraft Limit",
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for account in self.accounts:
                details = account.get_account_details()
                if isinstance(account, SavingsAccount):
                    details["Type"] = "Savings"
                    details["Interest Rate"] = account.interest_rate
                    details["Overdraft Limit"] = ""
                elif isinstance(account, CurrentAccount):
                    details["Type"] = "Current"
                    details["Interest Rate"] = ""
                    details["Overdraft Limit"] = account.overdraft_limit
                writer.writerow(details)

    def add_account(self, account):
        self.accounts.append(account)
        self.save_accounts()

    def find_account(self, account_number):
        for account in self.accounts:
            if account.get_account_details()["Account Number"] == account_number:
                return account
        return None
