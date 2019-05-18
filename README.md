# SparkPractice


## SparkSession vs SparkContext


### To make a new SparkSession:
    from pyspark.sql import SparkSession

    spark = SparkSession \
        .builder \
        .appName("Name") \
        .getOrCreate()