from repositories.account_repository import AccountRepository

class Account:
    def __init__(self, name, currency):
        self.name = name
        self.amount = 0.00
        self.currency = currency 

    def save(self):
        repository = AccountRepository("data/accounts.json")
        repository.save_account(self.__dict__)
