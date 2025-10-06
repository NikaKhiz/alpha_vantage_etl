### ETL Pipeline with Alpha Vantage

### Getting Started

1. **Clone the repository**:

   ```bash
   git clone https://github.com/NikaKhiz/alpha_vantage_etl.git
   cd alpha_vantage_etl
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**:

   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install all of the necessary libraries**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Generate .env file from .env.example and provide necessary variable values**:

   ```bash
   cp .env.example .env
   ```

## Usage

**Run scripts**:

- Simply run the `python main.py` command in the root directory:

```bash
python main.py
```

### the code above will fetch daily stock data from alpha vantage api, will be saved in json format, then after transformed and saved in to the database.
