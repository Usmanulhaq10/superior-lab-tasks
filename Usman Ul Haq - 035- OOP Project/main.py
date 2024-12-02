from bank_system import BankSystem
from savings_account import SavingsAccount
from current_account import CurrentAccount

def main_menu():
    bank = BankSystem()

    while True:
        print("\n--- Bank Management System ---")
        print("1. Add Savings Account")
        print("2. Add Current Account")
        print("3. Deposit Money")
        print("4. Withdraw Money") 
        print("5. Apply Interest (Savings Accounts)")
        print("6. Display Account Details")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder name: ")
            balance = float(input("Enter initial balance: "))
            interest_rate = float(input("Enter interest rate (e.g., 0.05 for 5%): "))
            account = SavingsAccount(account_number, account_holder, balance, interest_rate)
            bank.add_account(account)
            print("Savings account created successfully!")

        elif choice == "2":
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder name: ")
            balance = float(input("Enter initial balance: "))
            overdraft_limit = float(input("Enter overdraft limit: "))
            account = CurrentAccount(account_number, account_holder, balance, overdraft_limit)
            bank.add_account(account)
            print("Current account created successfully!")

        elif choice == "3":
            account_number = input("Enter account number: ")
            account = bank.find_account(account_number)
            if account:
                amount = float(input("Enter amount to deposit: "))
                print(account.deposit(amount))
                bank.save_accounts()
            else:
                print("Account not found.")

        elif choice == "4":
            account_number = input("Enter account number: ")
            account = bank.find_account(account_number)
            if account:
                amount = float(input("Enter amount to withdraw: "))
                print(account.withdraw(amount))
                bank.save_accounts()
            else:
                print("Account not found.")

        elif choice == "5":
            for account in bank.accounts:
                if isinstance(account, SavingsAccount):
                    print(account.apply_interest())
            bank.save_accounts()

        elif choice == "6":
            account_number = input("Enter account number: ")
            account = bank.find_account(account_number)
            if account:
                print(account.get_account_details())
            else:
                print("Account not found.")

        elif choice == "7":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

main_menu()
