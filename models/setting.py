class Setting:
    def __init__(self, base_currency):
        self.base_currency = base_currency

    def to_dict(self):
        return {
            'base_currency': self.base_currency
        }

    @staticmethod
    def from_dict(data):
        return Setting(
            base_currency=data['base_currency']
        )
