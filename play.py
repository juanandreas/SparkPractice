from spark_session import *

food_df = spark.read.csv("food.csv", inferSchema=True, header=True)
food_df.show()

