from pyspark.sql import SparkSession
from pyspark.sql.functions import col, length, trim
import os

print("Starting Spark session...")

spark = SparkSession.builder \
    .appName("GomalUrduETL") \
    .master("local[*]") \
    .config("spark.sql.warehouse.dir", "C:/tmp/spark-warehouse") \
    .getOrCreate()

try:
    print("Reading data/raw/urdu_wiki_raw.json...")
    df = spark.read.option("multiline", "true").json("data/raw/urdu_wiki_raw.json")    
    print("Original count:")
    df.show(5, truncate=100)
    
    # Clean - keep only Urdu text > 50 chars (500 was too high, you only have 4 docs)
    df_clean = df.filter(length(col("text")) > 50) \
                 .withColumn("text_clean", trim(col("text"))) \
                 .withColumn("text_len", length(col("text")))
    
    count = df_clean.count()
    print(f"Cleaned count: {count}")
    
    # Make sure folder exists
    os.makedirs("data/processed", exist_ok=True)
    
    # Save via Pandas (NO winutils needed) - BEST for Windows
    pandas_df = df_clean.toPandas()
    pandas_df.to_json("data/processed/urdu_wiki_clean.json", orient="records", force_ascii=False, indent=2)
    
    print("--- SAVED to data/processed/urdu_wiki_clean.json ---")
    print(f"Total {count} docs saved successfully!")

except Exception as e:
    print(f"Error: {e}")