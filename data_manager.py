import requests
from file_manager import FileManager


class DataManager:
    def __init__(self, api_key):
        self.base_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY'
        self.api_key = api_key
        self.headers = {'Content-Type': 'application/json'}
        self.file_manager = FileManager()

    def fetch_data(self, symbol):
        response = requests.get(
            self.base_url + f'&symbol={symbol}' + f'&apikey={self.api_key}', headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def save_data(self, filename, data):
        self.file_manager.write_to_file(filename, data)
