from database_manager import DatabaseManager
import os
from dotenv import load_dotenv
os.environ.clear()
load_dotenv()


def main():
    db_username = os.getenv('DB_USERNAME')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_name = os.getenv('DB_NAME', 'alpha_vantage_db')

    db_manager = DatabaseManager(db_host, db_username, db_password)
    db_manager.connect()
    db_manager.exists_or_create_database(db_name)

    print("ETL pipeline with alpha vantage :)")


if __name__ == '__main__':
    main()
