from models.account import Account
from repositories.account_repository import AccountRepository

class AccountService:
    def create_account(name, currency):
        account = Account(name, currency)
        account.save()

    def get_accounts():
        repository = AccountRepository("data/accounts.json")
        return repository.load_accounts()