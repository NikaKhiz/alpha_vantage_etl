import os
import json


class FileManager:
    def __init__(self):
        self.base_dir = "raw_data"

        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)

    def write_to_file(self, filename, data):
        file_path = os.path.join(self.base_dir, f"{filename}.json")
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def read_from_file(self, filename):
        file_path = os.path.join(self.base_dir, filename)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"No such file: {file_path}")
        with open(file_path, 'r') as file:
            return json.load(file)
