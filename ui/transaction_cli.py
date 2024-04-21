from services.transaction_service import TransactionService
from services.category_service import CategoryService
from tabulate import tabulate

class TransactionCLI:
    def __init__(self):
        self.transaction_service = TransactionService()
        self.category_service = CategoryService()

    def format_categories(self, categories):
        category_strings = [f"({cat.category_id}: {cat.name})" for cat in categories]
        return ', '.join(category_strings)

    def display_transactions(self, account_id):
        transactions = self.transaction_service.view_transactions(account_id)
        if transactions:
            transactions_data = [{"ID": tr.transaction_id, "Date": tr.date, "Category": tr.category_id, "Amount": tr.amount, "Comment": tr.comment} for tr in transactions]
            print(tabulate(transactions_data, headers="keys", tablefmt="grid"))
        else:
            print("No transactions to display.")

    def add_transaction(self, account_id):
        categories = self.category_service.view_categories(account_id)
        categories_string = self.format_categories(categories)
        date = input("Enter date: ")
        category_id = input(f"Enter category: {categories_string}")
        amount = input("Enter amount: ")
        comment = input("Enter comment: ")
        transaction = self.transaction_service.create_transaction(account_id, date, category_id, amount, comment)
        print(f"Transaction created: {transaction.transaction_id}")

    def update_transaction(self, account_id):
        categories = self.category_service.view_categories(account_id)
        categories_string = self.format_categories(categories)
        transaction_id = input("Enter transaction ID: ")
        date = input("Enter date: ")
        category_id = input(f"Enter category: {categories_string}")
        amount = input("Enter amount: ")
        comment = input("Enter comment: ")
        if self.transaction_service.update_transaction(transaction_id, account_id, date, category_id, amount, comment):
            print("Transaction updated successfully.")
        else:
            print("Transaction update failed.")
