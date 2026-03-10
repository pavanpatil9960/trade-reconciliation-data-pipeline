-- Internal Trades Table
CREATE TABLE internal_trades (
    trade_id VARCHAR(20),
    symbol VARCHAR(10),
    quantity INT,
    price DECIMAL(10,2),
    trade_date DATE
);

-- Broker Trades Table
CREATE TABLE broker_trades (
    trade_id VARCHAR(20),
    symbol VARCHAR(10),
    quantity INT,
    price DECIMAL(10,2),
    trade_date DATE
);

-- Reconciliation Results Table
CREATE TABLE reconciliation_results (
    trade_id VARCHAR(20),
    status VARCHAR(50),
    reconciliation_date DATE
);