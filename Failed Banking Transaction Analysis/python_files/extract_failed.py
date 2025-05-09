from pyspark.sql import SparkSession
#import mysql.connector

spark = SparkSession.builder.appName("FilterFailedTransactions").getOrCreate()

# Load cleaned file
df = spark.read.option("header", True).csv("gs://mohammed-bucket-1/processed/cleaned_transactions.csv/*.csv")

# Filter failed transactions
df_failed = df.filter(df.status == "FAILED")

# Write to Cloud SQL (MySQL)
jdbc_url = "jdbc:mysql://34.31.59.167:3306/project1"
properties = {
    "user": "admin",
    "password": "admin",
    "driver": "com.mysql.cj.jdbc.Driver"
}
df_failed.write.jdbc(url=jdbc_url, table="failed_transactions", mode="overwrite", properties=properties)


spark.stop()
