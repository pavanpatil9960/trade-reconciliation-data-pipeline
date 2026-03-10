# Trade Reconciliation Data Pipeline

## Project Overview

This project simulates a financial trade reconciliation process used in custodian banks and financial institutions.

Trade reconciliation is used to compare internal trade records with broker trade records to identify mismatches or missing trades.

The pipeline ingests trade data from two sources, performs reconciliation logic, and generates a reconciliation report highlighting any discrepancies.

---

## Architecture

Internal Trades CSV
        │
        │
        ▼
Python Data Processing
        │
        │
        ▼
Trade Reconciliation Logic
        │
        │
        ▼
Reconciliation Report

---

## Technologies Used

Python  
Pandas  
CSV Data Processing  
Git  
GitHub  

---

## Dataset

### Internal Trades

internal_trades.csv

Fields:

trade_id  
symbol  
quantity  
price  
trade_date  

---

### Broker Trades

broker_trades.csv

Fields:

trade_id  
symbol  
quantity  
price  
trade_date  

---

## Reconciliation Logic

The pipeline compares both datasets and identifies the following cases:

MATCH  
Trade exists in both datasets with same quantity and price.

PRICE_MISMATCH  
Trade price differs between internal and broker records.

QUANTITY_MISMATCH  
Trade quantity differs between internal and broker records.

MISSING_IN_BROKER  
Trade exists internally but not in broker records.

MISSING_IN_INTERNAL  
Trade exists in broker records but not internally.

---

## Output

Example reconciliation report:

trade_id | status
-------- | -------
T1001 | MATCH
T1002 | PRICE_MISMATCH
T1003 | QUANTITY_MISMATCH
T1004 | MISSING_IN_BROKER
T1005 | MISSING_IN_INTERNAL

The output file is generated as:

data/reconciliation_report.csv

---

## How to Run the Project

1 Navigate to project folder

2 Install required libraries

pip install pandas

3 Run reconciliation script

python scripts/reconciliation.py

4 Output will be generated in:

data/reconciliation_report.csv

---

## Future Improvements

Add AWS S3 data storage  
Implement PySpark for large scale data processing  
Load reconciled data into Snowflake  
Automate pipeline using Airflow