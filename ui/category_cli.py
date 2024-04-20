from services.category_service import CategoryService
from tabulate import tabulate

class CategoryCLI:
    def __init__(self):
        self.category_service = CategoryService()

    def display_categories(self, account_id):
        categories = self.category_service.view_categories(account_id)
        if categories:
            categories_data = [{"ID": cat.category_id, "Name": cat.name} for cat in categories]
            print(tabulate(categories_data, headers="keys", tablefmt="grid"))
        else:
            print("No categories to display.")

    def add_category(self, account_id):
        name = input("Enter name: ")
        category = self.category_service.create_category(account_id, name)
        print(f"Category created: {category.category_id}")

    def update_category(self, account_id):
        category_id = input("Enter category ID: ")
        name = input("Enter new name: ")
        if self.category_service.update_category(category_id, account_id, name):
            print("Category updated successfully.")
        else:
            print("Category update failed.")
