import mysql.connector


class DatabaseManager:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.connection = None
        self.cursor = None

    def connect(self):        # Code to establish a database connection
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.username,
            password=self.password
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):     # Code to close the database connection
        if self.cursor:
            self.cursor.close()
            self.cursor = None
        if self.connection:
            self.connection.close()
            self.connection = None

    # Code to check if a database exists or create it
    def exists_or_create_database(self, db_name):
        if self.cursor is None:
            raise Exception("Database not connected.")
        self.execute_query(f"CREATE DATABASE IF NOT EXISTS {db_name}")

    def use_database(self, db_name):  # Code to select a database
        if self.cursor is None:
            raise Exception("Database not connected.")
        self.execute_query(f"USE {db_name}")

    def create_table(self, table_name):  # Code to create a table
        if self.cursor is None:
            raise Exception("Database not connected.")

        create_table_sql = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            symbol VARCHAR(10) NOT NULL,
            date DATE NOT NULL,
            open_price FLOAT,
            high_price FLOAT,
            low_price FLOAT,
            close_price FLOAT,
            volume BIGINT,
            daily_change_percentage FLOAT,
            extraction_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(symbol, date)
        );
        """
        self.execute_query(create_table_sql)

    def insert_stock_data(self, df, table):
        if self.cursor is None:
            raise Exception("Database not connected.")

        insert_query = f"""
        INSERT INTO {table} (symbol, date, open_price, high_price, low_price, close_price, volume, daily_change_percentage, extraction_timestamp)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            open_price = VALUES(open_price),
            high_price = VALUES(high_price),
            low_price = VALUES(low_price),
            close_price = VALUES(close_price),
            volume = VALUES(volume),
            daily_change_percentage = VALUES(daily_change_percentage),
            extraction_timestamp = VALUES(extraction_timestamp);
        """
        for _, row in df.iterrows():
            data = (
                row['symbol'],
                row['date'],
                row['open'],
                row['high'],
                row['low'],
                row['close'],
                row['volume'],
                row['daily_change_percentage'],
                row['extraction_timestamp']
            )
            self.execute_query(insert_query, data)

    def execute_query(self, query, params=None):  # Code to execute a query
        if self.cursor is None:
            raise Exception("Database not connected.")
        self.cursor.execute(query, params or ())
        self.connection.commit()
