from ui.category_cli import CategoryCLI
from ui.transaction_cli import TransactionCLI
from services.account_service import AccountService
from services.transaction_service import TransactionService
from services.category_service import CategoryService
from tabulate import tabulate
from utils.helper import format_currency

class AccountCLI:
    def __init__(self):
        self.account_service = AccountService()
        self.transaction_service = TransactionService()
        self.category_service = CategoryService()
        self.category_cli = CategoryCLI()
        self.transaction_cli = TransactionCLI()

    def display_accounts(self):
        accounts = self.account_service.view_accounts()
        if accounts:
            accounts_data = [
                {"ID": acc.account_id, "Name": acc.name, "Balance": f"{format_currency(acc.amount, acc.currency)} {acc.currency}", "Is Saving?": acc.is_saving}
                for acc in accounts
            ]
            print(tabulate(accounts_data, headers="keys", tablefmt="grid"))
        else:
            print("No accounts to display.")

    def add_account(self):
        name = input("Enter name: ")
        currency = input("Enter currency: ")
        amount = float(input("Enter amount: "))
        is_saving = True if input("Is Saving Account (True/False): ").lower() == 'true' else False
        account = self.account_service.create_account(name, currency, amount, is_saving)
        print(f"Account created: {account.account_id}")

    def update_account(self):
        account_id = input("Enter account ID: ")
        name = input("Enter new name: ")
        currency = input("Enter new currency: ")
        is_saving = True if input("Is Saving Account (True/False): ").lower() == 'true' else False
        if self.account_service.update_account(account_id, name, currency, None, is_saving):
            print("Account updated successfully.")
        else:
            print("Account update failed.")

    def manage_account(self, account_id):
        commands = {
            '1': self.view_account_detail,
            '2': self.category_cli.display_categories,
            '3': self.category_cli.add_category,
            '4': self.category_cli.update_category,
            '5': self.transaction_cli.display_transactions,
            '6': self.transaction_cli.add_transaction,
            '7': self.transaction_cli.update_transaction,
            '0': 'return'
        }
        while True:
            choice = input("""
1. View Account Detail
2. Display Categories
3. Add Category
4. Update Category
5. Display Transactions
6. Add Transaction
7. Update Transaction
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
        account = self.account_service.find_account_by_id(account_id)
        if account:
            transactions = self.transaction_service.view_transactions(account_id)
            
            account_data = [
                {"Information": "Account ID", "Value": account.account_id},
                {"Information": "Name", "Value": account.name},
                {"Information": "Is Saving", "Value": account.is_saving},
                {"Information": "Balance", "Value": f"{format_currency(account.amount, account.currency)} {account.currency}"}
            ]

            if (account.is_saving == False):
                income_transactions = [t for t in transactions if t.category_id is '1']
                account_data.append({"Information": "Total Income", "Value": f"{format_currency(sum(float(t.amount) for t in income_transactions), account.currency)} {account.currency}"})

            print(tabulate(account_data, headers="keys", tablefmt="grid"))

            if (account.is_saving == False):
                debit_transactions = [t for t in transactions if t.category_id is not '1']
                total_expenses = sum(float(t.amount) for t in debit_transactions)

                expenses_by_category = {}
                for trans in debit_transactions:
                    if trans.category_id in expenses_by_category:
                        expenses_by_category[trans.category_id]['amount'] += float(trans.amount)
                        expenses_by_category[trans.category_id]['count'] += 1
                    else:
                        expenses_by_category[trans.category_id] = {}
                        expenses_by_category[trans.category_id]['amount'] = float(trans.amount)
                        expenses_by_category[trans.category_id]['count'] = 1

                if expenses_by_category:
                    expense_data = [
                        {
                            "Category": self.category_service.find_category_by_id(category_id, account_id).name,
                            "Total Expenses": f"{format_currency(expenses['amount'], account.currency)} {account.currency}",
                            "Number of Transactions": expenses['count'],
                            "Percentage": f"{(expenses['amount'] / total_expenses * 100):.2f}%"
                        } for category_id, expenses in expenses_by_category.items()
                    ]
                    print("\nExpense Report by Category:")
                    print(tabulate(expense_data, headers="keys", tablefmt="grid"))
        else:
            print("No accounts to display.")
