from utils.file_handler import read_json, write_json
from models.transaction import Transaction
from datetime import datetime

class TransactionRepository:
    def __init__(self, filename='data/transactions.json'):
        self.filename = filename

    def set_storage_filename(self, filename):
        self.filename = filename

    def load_transactions(self, account_id):
        transactions_data = read_json(self.filename)
        transactions = [Transaction.from_dict(transaction) for transaction in transactions_data if transaction['account_id'] == account_id]
        return sorted(transactions, key=lambda tra: datetime.strptime(tra.date, '%d/%m/%Y').date())

    def save_transactions(self, transactions):
        transactions_data = [transaction.to_dict() for transaction in transactions]
        write_json(transactions_data, self.filename)

    def find_transaction_by_id(self, transaction_id, account_id):
        transactions = self.load_transactions(account_id)
        for transaction in transactions:
            if transaction.transaction_id == transaction_id:
                return transaction
        return None

    def update_transaction(self, updated_transaction, account_id):
        transactions = self.load_transactions(account_id)
        for i, transaction in enumerate(transactions):
            if transaction.transaction_id == updated_transaction.transaction_id:
                transactions[i] = updated_transaction
                self.save_transactions(transactions)
                return True
        return False
