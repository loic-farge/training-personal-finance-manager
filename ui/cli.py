from services.account_service import AccountService
import pandas as pd

class CLI:
    def __init__(self):
        self.running = True

    def start(self):
        print("Welcome to the Personal Finance Manager!")
        while self.running:
            command = input("Enter command (type 'help' for options or 'exit' to quit): ").strip().lower()
            if command == 'exit':
                self.running = False
                print("Thank you for using the Personal Finance Manager. Goodbye!")
            elif command == 'help':
                self.display_help()
            else:
                self.process_command(command)

    def process_command(self, command_input):
        parts = command_input.split(maxsplit=1)
        command = parts[0]
        arguments = parts[1] if len(parts) > 1 else ""

        if command == 'create_account':
            args = arguments.split();
            AccountService.create_account(args[0], args[1])
            print("Account has been created")
        elif command == 'view_accounts':
            print(pd.DataFrame(AccountService.get_accounts()))
        else:
            print("Unknown command. Type 'help' for a list of commands.")

    def display_help(self):
        print("""
Available commands:
- create_account: Add a new account
- exit: Exit the program
        """)