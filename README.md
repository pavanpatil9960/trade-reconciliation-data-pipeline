# Trade Reconciliation Data Pipeline

## Project Overview

This project simulates a financial trade reconciliation process used in custodian banks and financial institutions.

Trade reconciliation compares internal trade records with broker trade confirmations to detect mismatches, missing trades, or incorrect values.

This project simulates how financial institutions reconcile trade data between internal systems and broker confirmations using data engineering pipelines.

---

## Data Pipeline Architecture

```
                +-------------------+
                | Internal Trades   |
                | CSV File          |
                +-------------------+
                         |
                         |
                         v
                +-------------------+
                | Python / PySpark  |
                | Data Processing   |
                +-------------------+
                         |
                         |
                         v
                +-------------------+
                | Reconciliation    |
                | Logic             |
                +-------------------+
                         |
                         |
                         v
                +-------------------+
                | Reconciliation    |
                | Report CSV        |
                +-------------------+
```

---

## Technologies Used

* Python
* Pandas
* PySpark
* SQL
* Git
* GitHub

---

## Dataset

### Internal Trades

File: `internal_trades.csv`

Fields:

* trade_id
* symbol
* quantity
* price
* trade_date

---

### Broker Trades

File: `broker_trades.csv`

Fields:

* trade_id
* symbol
* quantity
* price
* trade_date

---

## Reconciliation Logic

The pipeline compares internal trades and broker trades and identifies the following scenarios:

**MATCH**
Trade exists in both datasets with the same quantity and price.

**PRICE_MISMATCH**
Trade price differs between internal and broker records.

**QUANTITY_MISMATCH**
Trade quantity differs between internal and broker records.

**MISSING_IN_BROKER**
Trade exists internally but not in broker records.

**MISSING_IN_INTERNAL**
Trade exists in broker records but not internally.

---

## Output

Example reconciliation report:

```
trade_id | status
--------------------------
T1001    | MATCH
T1002    | PRICE_MISMATCH
T1003    | QUANTITY_MISMATCH
T1004    | MISSING_IN_BROKER
T1005    | MISSING_IN_INTERNAL
```

Generated output files:

* `data/reconciliation_report.csv`
* `data/pyspark_reconciliation_report.csv`

---

## How to Run the Project

### 1 Navigate to project folder

```
cd trade-reconciliation-data-pipeline
```

### 2 Install required libraries

```
pip install -r requirements.txt
```

### 3 Run the Python reconciliation pipeline

```
python scripts/reconciliation.py
```

### 4 Run the PySpark reconciliation pipeline

```
python scripts/pyspark_reconciliation.py
```

Reconciliation reports will be generated inside the `data` folder.

---

## SQL Data Warehouse Schema

The project also includes SQL table definitions to simulate how trade data would be stored in a data warehouse.

Tables:

* internal_trades
* broker_trades
* reconciliation_results

SQL script location:

```
sql/create_tables.sql
```

---

## Project Structure

```
trade-reconciliation-data-pipeline
│
├── data
│   ├── internal_trades.csv
│   ├── broker_trades.csv
│   ├── reconciliation_report.csv
│   └── pyspark_reconciliation_report.csv
│
├── scripts
│   ├── reconciliation.py
│   └── pyspark_reconciliation.py
│
├── sql
│   └── create_tables.sql
│
├── requirements.txt
└── README.md
```

---

## Future Improvements

* Store trade data in a database instead of CSV files
* Load data into a data warehouse such as Snowflake
* Automate pipeline scheduling using Apache Airflow
* Store reconciliation results in a reporting table for dashboards

---

## Author

Data Engineering portfolio project demonstrating trade data reconciliation workflows commonly used in financial institutions.
