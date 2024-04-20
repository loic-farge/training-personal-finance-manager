from services.setting_service import SettingService
from tabulate import tabulate

class SettingCLI:
    def __init__(self):
        self.setting_service = SettingService()

    def display_settings(self):
        settings = self.setting_service.view_settings()
        if settings:
            settings_data = [{"Name": "Base Currency", "Value": setting.base_currency} for setting in settings]
            print(tabulate(settings_data, headers="keys", tablefmt="grid"))
        else:
            print("No settings to display.")

    def update_settings(self):
        base_currency = input("Enter Base Currency: ")
        self.setting_service.update_settings(base_currency)
        print("Settings have been updated")
