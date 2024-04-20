class Category:
    def __init__(self, account_id, name, category_id=None):
        self.account_id = account_id
        self.name = name
        self.category_id = category_id      

    def to_dict(self):
        return {
            'account_id': self.account_id,
            'name': self.name,
            'category_id': self.category_id
        }

    @staticmethod
    def from_dict(data):
        return Category(
            account_id=data['account_id'],
            name=data['name'],
            category_id=data['category_id']
        )
