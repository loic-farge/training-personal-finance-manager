from utils.file_handler import read_json, write_json
from models.category import Category

class CategoryRepository:
    def __init__(self, filename='data/categories.json'):
        self.filename = filename

    def set_storage_filename(self, filename):
        self.filename = filename

    def load_categories(self, account_id):
        categories_data = read_json(self.filename)
        categories = [Category.from_dict(category) for category in categories_data if category['account_id'] == account_id]
        return sorted(categories, key=lambda cat: int(cat.category_id))

    def save_categories(self, categories):
        categories_data = [category.to_dict() for category in categories]
        write_json(categories_data, self.filename)

    def find_category_by_id(self, category_id, account_id):
        categories = self.load_categories(account_id)
        for category in categories:
            if category.category_id == category_id:
                return category
        return None

    def update_category(self, updated_category, account_id):
        categories = self.load_categories(account_id)
        for i, category in enumerate(categories):
            if category.category_id == updated_category.category_id:
                categories[i] = updated_category
                self.save_categories(categories)
                return True
        return False
