from repositories.category_repository import CategoryRepository
from models.category import Category
import uuid

class CategoryService:
    def __init__(self):
        self.repository = CategoryRepository()

    def update_account_filename(self, account_id):
        self.repository.set_storage_filename(f"data/{account_id}/categories.json")

    def create_category(self, account_id, name):
        self.update_account_filename(account_id)
        categories = self.view_categories(account_id)
        if categories:
            category_id = max(int(cat.category_id) for cat in categories) + 1
        else:
            category_id = 1
        new_category = Category(account_id, name, category_id)
        categories = self.repository.load_categories(account_id)
        categories.append(new_category)
        self.repository.save_categories(categories)
        return new_category

    def view_categories(self, account_id):
        self.update_account_filename(account_id)
        categories = self.repository.load_categories(account_id)
        return categories

    def update_category(self, category_id, account_id, name):
        self.update_account_filename(account_id)
        category = self.repository.find_category_by_id(category_id, account_id)
        if category:
            category.account_id = account_id
            category.name = name
            return self.repository.update_category(category, account_id)
        return False
    
    def find_category_by_id(self, category_id, account_id):
        self.update_account_filename(account_id)
        return self.repository.find_category_by_id(category_id, account_id)
