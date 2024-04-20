from ui.category_cli import CategoryCLI
from services.account_service import AccountService
from tabulate import tabulate

class AccountCLI:
    def __init__(self):
        self.account_service = AccountService()
        self.category_cli = CategoryCLI()

    def display_accounts(self):
        accounts = self.account_service.view_accounts()
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
        account = self.account_service.create_account(name, currency, amount)
        print(f"Account created: {account.account_id}")

    def update_account(self):
        account_id = input("Enter account ID: ")
        name = input("Enter new name: ")
        currency = input("Enter new currency: ")
        if self.account_service.update_account(account_id, name, currency):
            print("Account updated successfully.")
        else:
            print("Account update failed.")

    def manage_account(self, account_id):
        commands = {
            '1': self.view_account_detail,
            '2': self.category_cli.display_categories,
            '3': self.category_cli.add_category,
            '4': self.category_cli.update_category,
            '0': 'return'
        }
        while True:
            choice = input("""
1. View Account Detail
2. Display Categories
3. Add Category
4. Update Category
0. Return to Main Menu
""")
            action = commands.get(choice)
            if action == 'return':
                return
            elif action:
                action(account_id)
            else:
                print("Invalid option")

    def view_account_detail(self, account_id):
        # Method to view account details
        pass

    # Other methods
