import pandas as pd
# Load datasets
internal = pd.read_csv('D:/trade-reconciliation-data-pipeline/data/internal_trades.csv')
broker = pd.read_csv('D:/trade-reconciliation-data-pipeline/data/broker_trades.csv')

# Merge datasets
df = pd.merge(internal, broker, on='trade_id', how='outer', suffixes=('_internal', '_broker'))

# Function to identify issues
def check_issue(row):
    if pd.isna(row['symbol_internal']):
        return 'MISSING_IN_INTERNAL'
    
    if pd.isna(row['symbol_broker']):
        return 'MISSING_IN_BROKER'
    
    if row['price_internal'] != row['price_broker']:
        return 'PRICE_MISMATCH'
    
    if row['quantity_internal'] != row['quantity_broker']:
        return 'QUANTITY_MISMATCH'
    
    return 'MATCH'

df['status'] = df.apply(check_issue, axis=1)

print(df[['trade_id', 'status']])

df[['trade_id', 'status']].to_csv('D:/trade-reconciliation-data-pipeline/data/reconciliation_report.csv', index=False)