from ui.account_cli import AccountCLI
from ui.category_cli import CategoryCLI
from ui.transaction_cli import TransactionCLI
from ui.setting_cli import SettingCLI

class MainCLI:
    def __init__(self):
        self.account_cli = AccountCLI()
        self.category_cli = CategoryCLI()
        self.transaction_cli = TransactionCLI()
        self.setting_cli = SettingCLI()
    
    def main_menu(self):
        while True:
            print("""MANAGE ACCOUNTS
----------------------
1. Display Accounts
2. Add Account
3. Update Account
4. Manage Account
----------------------
MANAGE SETTINGS
----------------------
98. Display Settings
99. Update Settings
----------------------
0. Exit
""")
            choice = input("Choose an option: ")
            if choice == '1':
                self.account_cli.display_accounts()
            elif choice == '2':
                self.account_cli.add_account()
            elif choice == '3':
                self.account_cli.update_account()
            elif choice == '4':
                account_id = input("Enter Account ID: ")
                self.account_cli.manage_account(account_id)
            elif choice == '98':
                self.setting_cli.display_settings()
            elif choice == '99':
                self.setting_cli.update_settings()
            elif choice == '0':
                print("Thank you for using the finance manager. Goodbye!")
                break
            else:
                print("Invalid option")

    def run(self):
        self.main_menu()
