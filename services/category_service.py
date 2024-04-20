from repositories.category_repository import CategoryRepository
from models.category import Category
import uuid

class CategoryService:
    def __init__(self):
        self.repository = CategoryRepository()

    def create_category(self, account_id, name):
        category_id = uuid.uuid4().hex
        new_category = Category(account_id, name, category_id)
        categories = self.repository.load_categories()
        categories.append(new_category)
        self.repository.save_categories(categories)
        return new_category

    def view_categories(self):
        categories = self.repository.load_categories()
        return categories

    def update_category(self, category_id, name):
        category = self.repository.find_category_by_id(category_id)
        if category:
            category.name = name
            return self.repository.update_category(category)
        return False
