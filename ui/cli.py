from services.account_service import AccountService
from tabulate import tabulate

class CLI:
    def __init__(self):
        self.service = AccountService()

    def display_accounts(self):
        accounts = self.service.view_accounts()
        if accounts:
            accounts_data = [
                {"ID": acc.account_id, "Name": acc.name, "Currency": acc.currency, "Amount": acc.amount}
                for acc in accounts
            ]
            print(tabulate(accounts_data, headers="keys", tablefmt="grid"))
        else:
            print("No accounts to display.")

    def add_account(self):
        name = input("Enter name: ")
        currency = input("Enter currency: ")
        amount = float(input("Enter amount: "))
        account = self.service.create_account(name, currency, amount)
        print(f"Account created: {account.account_id}")

    def update_account(self):
        account_id = input("Enter account ID: ")
        name = input("Enter new name: ")
        currency = input("Enter new currency: ")
        if self.service.update_account(account_id, name, currency):
            print("Account updated successfully.")
        else:
            print("Account update failed.")

    def run(self):
        commands = {
            '1': self.display_accounts,
            '2': self.add_account,
            '3': self.update_account,
            '0': self.exit_cli
        }
        while True:
            choice = input("""MANAGE ACCOUNTS
----------------------
1. Display Accounts
2. Add Account
3. Update Account
----------------------
0. Exit
 Choose an option: """)
            action = commands.get(choice)
            if action:
                action()
            else:
                print("Invalid option")

    def exit_cli(self):
        print("Thank you for using the finance manager. Goodbye!")
        exit(0)
