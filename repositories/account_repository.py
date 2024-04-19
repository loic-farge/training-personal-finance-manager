from utils.file_handler import load_json, save_json, ensure_file_exists

class AccountRepository:
    def __init__(self, filename):
        self.filename = filename
        ensure_file_exists(filename)

    def save_account(self, account):
        self.save_accounts(self.load_accounts() + [account])

    def save_accounts(self, accounts):
        accounts_data = [account for account in accounts]
        save_json(accounts_data, self.filename)

    def load_accounts(self):
        accounts_data = load_json(self.filename)
        return accounts_data