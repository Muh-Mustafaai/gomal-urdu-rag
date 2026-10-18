from pyspark.sql import SparkSession
from pyspark.sql.functions import col, length, trim

print("Starting Spark session...")

spark = SparkSession.builder \
    .appName("GomalUrduETL") \
    .master("local[*]") \
    .getOrCreate()

try:
    print("Reading data/raw/urdu_wiki_raw.json...")
    df = spark.read.json("data/raw/urdu_wiki_raw.json")
    
    print("Original count:")
    df.show(5)
    
    # Clean
    df_clean = df.filter(length(col("text")) > 500) \
                 .withColumn("text_clean", trim(col("text"))) \
                 .withColumn("text_len", length(col("text")))
    
    print(f"Cleaned count: {df_clean.count()}")
    
    df_clean.write.mode("overwrite").parquet("data/processed/urdu_wiki_clean.parquet")
    df_clean.write.mode("overwrite").json("data/processed/urdu_wiki_clean.json")
    
    print("--- SAVED to data/processed/urdu_wiki_clean.parquet ---")

except Exception as e:
    print(f"Error: {e}")
    print("If json not found, run scraper first!")

spark.stop()