class Transaction:
    def __init__(self, account_id, date, category_id, amount, comment=None, transaction_id=None):
        self.account_id = account_id
        self.date = date
        self.category_id = category_id  
        self.amount = amount 
        self.comment = comment 
        self.transaction_id = transaction_id     

    def to_dict(self):
        return {
            'account_id': self.account_id,
            'date': self.date,
            'category_id': self.category_id,
            'amount': self.amount,
            'comment': self.comment,
            'transaction_id': self.transaction_id
        }

    @staticmethod
    def from_dict(data):
        return Transaction(
            account_id=data['account_id'],
            date=data['date'],
            category_id=data['category_id'],
            amount=data['amount'],
            comment=data['comment'],
            transaction_id=data['transaction_id']
        )
