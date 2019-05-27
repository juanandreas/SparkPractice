from pyspark.sql import SparkSession

spark = SparkSession\
    .builder\
    .appName("play")\
    .getOrCreate()

food_df = spark.read.csv("food.csv", inferSchema=True, header=True)
food_df.show()



food_df.createOrReplaceTempView("food_df")

df = spark.sql("""
    SELECT * from food_df
    WHERE Type = 'Animal'
""")

df.show()

spark.stop()

