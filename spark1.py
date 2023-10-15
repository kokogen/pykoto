from datetime import datetime, date
import pandas as pd
from pyspark.sql import Row
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('spark1-app').getOrCreate()

m = [
    (1, 'google.com', date(2020, 1, 2), ),
]

df = spark.createDataFrame([
    (1, 2., 'string1', date(2000, 1, 1), datetime(2000, 1, 1, 12, 0)),
    (2, 3., 'string2', date(2000, 2, 1), datetime(2000, 1, 2, 12, 0)),
    (3, 4., 'string3', date(2000, 3, 1), datetime(2000, 1, 3, 12, 0))
], schema='a long, b double, c string, d date, e timestamp')

df.printSchema()


