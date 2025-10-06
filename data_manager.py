import requests
from file_manager import FileManager
from typing import Dict
from pydantic import BaseModel, Field, ValidationError


class DailyData(BaseModel):
    open: float = Field(alias="1. open")
    high: float = Field(alias="2. high")
    low: float = Field(alias="3. low")
    close: float = Field(alias="4. close")
    volume: int = Field(alias="5. volume")


class MetaData(BaseModel):
    information: str = Field(alias="1. Information")
    symbol: str = Field(alias="2. Symbol")
    last_refreshed: str = Field(alias="3. Last Refreshed")
    output_size: str = Field(alias="4. Output Size")
    time_zone: str = Field(alias="5. Time Zone")


class StockApiResponse(BaseModel):
    meta_data: MetaData = Field(alias="Meta Data")
    time_series: Dict[str, DailyData] = Field(alias="Time Series (Daily)")


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
            try:
                validated_data = StockApiResponse(**response.json())
                return validated_data
            except ValidationError as e:
                print("Validation error:", e)
                return None
        else:
            response.raise_for_status()

    def save_data(self, filename, data):
        self.file_manager.write_to_file(filename, data.dict(by_alias=True))
