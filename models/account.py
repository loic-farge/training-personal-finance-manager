class Account:
    def __init__(self, name, currency, amount, account_id=None):
        self.name = name
        self.currency = currency
        self.amount = amount
        self.account_id = account_id

    def to_dict(self):
        return {
            'name': self.name,
            'currency': self.currency,
            'amount': self.amount,
            'account_id': self.account_id
        }

    @staticmethod
    def from_dict(data):
        return Account(
            name=data['name'],
            currency=data['currency'],
            amount=data['amount'],
            account_id=data['account_id']
        )
