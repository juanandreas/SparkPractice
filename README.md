# SparkPractice


### To make a new SparkSession:
    from pyspark.sql import SparkSession

    spark = SparkSession \
        .builder \
        .appName("Name") \
        .getOrCreate()
        
        
## SparkSession vs SparkContext
   Prior to Spark 2.0.0 sparkContext was used as a channel to access all spark functionality.

   SPARK 2.0.0 onwards, SparkSession provides a single point of entry to interact with 
   underlying Spark functionality and allows programming Spark with DataFrame and Dataset APIs. 
   All the functionality available with sparkContext are also available in sparkSession.