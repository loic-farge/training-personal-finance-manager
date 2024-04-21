from repositories.account_repository import AccountRepository
from models.account import Account
import uuid

class AccountService:
    def __init__(self):
        self.repository = AccountRepository()

    def create_account(self, name, currency, amount, is_saving=False):
        account_id = uuid.uuid4().hex
        new_account = Account(name, currency, amount, is_saving, account_id)
        accounts = self.repository.load_accounts()
        accounts.append(new_account)
        self.repository.save_accounts(accounts)
        return new_account

    def view_accounts(self):
        accounts = self.repository.load_accounts()
        return accounts

    def update_account(self, account_id, name, currency, amount=None, is_saving=False):
        account = self.repository.find_account_by_id(account_id)
        if account:
            account.name = name
            account.currency = currency
            account.is_saving = is_saving
            if amount is not None:
                account.amount = amount
            return self.repository.update_account(account)
        return False
    
    def find_account_by_id(self, account_id):
        return self.repository.find_account_by_id(account_id)
