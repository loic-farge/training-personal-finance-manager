from repositories.transaction_repository import TransactionRepository
from services.account_service import AccountService
from models.transaction import Transaction
import uuid

class TransactionService:
    def __init__(self):
        self.repository = TransactionRepository()
        self.account_service = AccountService()

    def update_account_filename(self, account_id):
        self.repository.set_storage_filename(f"data/{account_id}/transactions.json")

    def create_transaction(self, account_id, date, category_id, amount, comment=None):
        self.update_account_filename(account_id)
        transaction_id = uuid.uuid4().hex
        new_transaction = Transaction(account_id, date, category_id, amount, comment, transaction_id)
        transactions = self.repository.load_transactions(account_id)
        transactions.append(new_transaction)
        self.repository.save_transactions(transactions)
        self.update_account_amount(account_id)
        return new_transaction

    def view_transactions(self, account_id):
        self.update_account_filename(account_id)
        transactions = self.repository.load_transactions(account_id)
        return transactions

    def update_transaction(self, transaction_id, account_id, date, category_id, amount, comment):
        self.update_account_filename(account_id)
        transaction = self.repository.find_transaction_by_id(transaction_id, account_id)
        if transaction:
            transaction.account_id = account_id
            transaction.date = date
            transaction.category_id = category_id
            transaction.amount = amount
            transaction.comment = comment
            updated_transaction = self.repository.update_transaction(transaction, account_id)
            self.update_account_amount(account_id)
            return updated_transaction
        return False
    
    def update_account_amount(self, account_id):
        transactions = self.view_transactions(account_id)
        total = sum(float(transaction.amount) for transaction in transactions)
        account = self.account_service.find_account_by_id(account_id)
        if account:
            self.account_service.update_account(account.account_id, account.name, account.currency, total)

