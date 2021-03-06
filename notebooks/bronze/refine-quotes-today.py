# %%
# Set the Datalake Access Key configuration
spark.conf.set(
    "fs.azure.account.key.cryptoanalyticslake.dfs.core.windows.net",
    dbutils.secrets.get(scope="key-vault-secret-scope",key="cryptoanalyticslake-access-key"))

# %%
# Set Day Month Year
from datetime import datetime, timedelta

today = datetime.utcnow()
year = today.year
month = today.month
day = today.day

# %%
# Recursive data load for all files from a day from every partition in the Event Hub Namespace
sourcefolderpath = f"abfss://crypto-quotes@cryptoanalyticslake.dfs.core.windows.net/ehns-quote-streams/eh-crypto-stream/*/{year}/{month:0>2d}/{day:0>2d}"

print(sourcefolderpath)

df = spark.read.option("recursiveFileLookup","true").option("header","true").format("avro").load(sourcefolderpath)

# %%
# Change the Body field from Binary to JSON 
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StringType, DoubleType, StructType, StructField

sourceSchema = StructType([
        StructField("Symbol", StringType(), False),
        StructField("Price", DoubleType(), True),
        StructField("PriceTimeStamp", StringType(), True)])

df = df.withColumn("StringBody", col("Body").cast("string"))
jsonOptions = {"dateFormat" : "yyyy-MM-dd HH:mm:ss.SSS"}
df = df.withColumn("JsonBody", from_json(df.StringBody, sourceSchema, jsonOptions))

# %%
# Flattent he Body JSON field into columns of the DataFrame
for c in df.schema["JsonBody"].dataType:
    df = df.withColumn(c.name, col("JsonBody." + c.name))

# %%
# Remove 0 priced assets
df = df.filter("Price > 0")

# %%
# Sort the data
df = df.sort("Symbol", "PriceTimeStamp")

# %%
# Select only the meaningful columns for the export to Bronze data zone
exportDF = df.select("Symbol", "Price", "PriceTimeStamp")

# %%
# Add Price Date column
from pyspark.sql.functions import to_date, to_timestamp
from pyspark.sql.types import *

exportDF = exportDF.withColumn("PriceDate", to_date("PriceTimeStamp")) \
                   .withColumn("PriceTimeStamp", to_timestamp("PriceTimeStamp")) \
                   .withColumn("Price", df.Price.cast(DecimalType(38,15)))

# %%
# Write the parquet file in the bronze crypto data zone
sparkpartitionfolderpath = f"abfss://crypto-bronze@cryptoanalyticslake.dfs.core.windows.net/quotes-by-day-spark-partition"

print(sparkpartitionfolderpath)

exportDF.write.partitionBy("PriceDate").mode("overwrite").parquet(sparkpartitionfolderpath)

# %%
# Write the parquet file in the bronze crypto data zone
manualpartitionfolderpath = f"abfss://crypto-bronze@cryptoanalyticslake.dfs.core.windows.net/quotes-by-day-manual-partition/{year}/{month:0>2d}/{day:0>2d}"

print(manualpartitionfolderpath)

exportDF.write.mode("overwrite").parquet(manualpartitionfolderpath)


