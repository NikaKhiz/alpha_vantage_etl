from database_manager import DatabaseManager
from data_manager import DataManager
import os
from dotenv import load_dotenv
os.environ.clear()
load_dotenv()


def main():
    db_username = os.getenv('DB_USERNAME')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_name = os.getenv('DB_NAME', 'alpha_vantage_db')

    api_key = os.getenv('ALPHA_VANTAGE_API_KEY')

    SYMBOLS = ['AAPL', 'GOOG', 'MSFT']

    data_manager = DataManager(api_key=api_key)

    for symbol in SYMBOLS:
        data = data_manager.fetch_data(symbol=symbol)
        data_manager.save_data(
            f'{symbol}_' + data.meta_data.last_refreshed, data)

    db_manager = DatabaseManager(db_host, db_username, db_password)
    db_manager.connect()
    db_manager.exists_or_create_database(db_name)
    db_manager.use_database(db_name)
    db_manager.create_table('stock_daily_data')

    for file in os.listdir('raw_data'):
        transformed_data = data_manager.transform_data(
            data_manager.file_manager.read_from_file(file))

    db_manager.disconnect()

    print("ETL pipeline with alpha vantage :)")


if __name__ == '__main__':
    main()
