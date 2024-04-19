import json
import os

def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def save_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def ensure_file_exists(filename):
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                f.write('[]')