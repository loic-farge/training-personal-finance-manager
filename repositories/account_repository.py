from utils.file_handler import read_json, write_json
from models.account import Account

class AccountRepository:
    def __init__(self, filename='data/accounts.json'):
        self.filename = filename

    def load_accounts(self):
        accounts_data = read_json(self.filename)
        return [Account.from_dict(account) for account in accounts_data]

    def save_accounts(self, accounts):
        accounts_data = [account.to_dict() for account in accounts]
        write_json(accounts_data, self.filename)

    def find_account_by_id(self, account_id):
        accounts = self.load_accounts()
        for account in accounts:
            if account.account_id == account_id:
                return account
        return None

    def update_account(self, updated_account):
        accounts = self.load_accounts()
        for i, account in enumerate(accounts):
            if account.account_id == updated_account.account_id:
                accounts[i] = updated_account
                self.save_accounts(accounts)
                return True
        return False
