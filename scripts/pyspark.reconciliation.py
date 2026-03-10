from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

# Create Spark session
spark = SparkSession.builder.appName("TradeReconciliation").getOrCreate()

# Load datasets
intenal_df = spark.read.csv("D:/trade-reconciliation-data-pipeline/data/internal_trades.csv", header=True, inferSchema=True)
broker_df = spark.read.csv("D:/trade-reconciliation-data-pipeline/data/broker_trades.csv", header=True, inferSchema=True)

# Join datasets
df = intenal_df.alias("i").join(
    broker_df.alias("b"),
    col("i.trade_id") == col("b.trade_id"),
    "full_outer"
)

# Reconciliation logic
result = df.withColumn(
    "status",
    when(col("i.trade_id").isNull(), "MISSING_IN_INTERNAL")
    .when(col("b.trade_id").isNull(), "MISSING_IN_BROKER")
    .when(col("i.price") != col("b.price"), "PRICE_MISMATCH")
    .when(col("i.quantity") != col("b.quantity"), "QUANTITY_MISMATCH")
    .otherwise("MATCH")
)

# Select output columns
output = result.select(
    col("i.trade_id").alias("internal_trade_id"),
    col("b.trade_id").alias("broker_trade_id"),
    "status"
    )

# Show result
output.show()

# Save output
output.toPandas().to_csv("D:/trade-reconciliation-data-pipeline/data/pyspkark_reconciliation_report.csv", index=False)