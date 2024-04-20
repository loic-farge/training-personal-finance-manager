from utils.file_handler import read_json, write_json
from models.setting import Setting

class SettingRepository:
    def __init__(self, filename='data/settings.json'):
        self.filename = filename

    def load_settings(self):
        settings_data = read_json(self.filename)
        return [Setting.from_dict(setting) for setting in settings_data]

    def save_settings(self, settings):
        settings_data = [settings.to_dict()]
        write_json(settings_data, self.filename)
