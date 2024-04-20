from repositories.setting_repository import SettingRepository
from models.setting import Setting

class SettingService:
    def __init__(self):
        self.repository = SettingRepository()

    def update_settings(self, base_currency):
        new_setting = Setting(base_currency)
        self.repository.save_settings(new_setting)
        return new_setting

    def view_settings(self):
        settings = self.repository.load_settings()
        return settings
