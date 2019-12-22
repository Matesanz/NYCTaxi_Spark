import pandas as pd
import seaborn as sns
from sodapy import Socrata
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# initialize SparkSession
sparkSession = SparkSession\
    .builder\
    .master("local[8]")\
    .appName('NYC Taxis January 2019')\
    .getOrCreate()

# Import csv data
dataset = sparkSession\
    .read\
    .options(header='true', inferschema='true')\
    .format("csv")\
    .load("data/2019_Yellow_Taxi_Trip_Data.csv")

#dataset.show()
dataset.printSchema()

filt = dataset.select("tpep_pickup_datetime", "tpep_dropoff_datetime", "trip_distance", "fare_amount")
filt = filt.filter(dataset.trip_distance != 0.00)

data_frame = filt.withColumn("tpep_pickup_datetime",F.to_timestamp("tpep_pickup_datetime","MM/dd/yyyy HH:mm:ss"))
data_frame = data_frame.withColumn("tpep_dropoff_datetime",F.to_timestamp("tpep_dropoff_datetime","MM/dd/yyyy HHHH:mm:ss"))

data_frame_january = data_frame.where(F.col("tpep_pickup_datetime").between("2018-01-01",  "2019-01-15"))
print((data_frame_january.count(), len(data_frame_january.columns)))

data_frame_january.show(10)

pd_dataset = data_frame_january.toPandas()
pd_dataset['tpep_pickup_datetime'] = pd_dataset['tpep_pickup_datetime'].astype('datetime64[ns]')
pd_dataset.head()

pd_dataset.count()

sparkSession.stop()