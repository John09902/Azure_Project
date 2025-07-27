# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window

# COMMAND ----------

# MAGIC %md
# MAGIC ### **Data Reading**

# COMMAND ----------

df = spark.read.format("parquet")\
        .load("abfss://bronze@databricksete.dfs.core.windows.net/orders")

# COMMAND ----------

display(df)

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df = df.drop("_rescued_data")
df.display()

# COMMAND ----------

df = df.withColumn("order_date",to_timestamp(col('order_date')))
df.display()

# COMMAND ----------

df = df.withColumn("year",year(col('order_date')))
df.display()

# MAGIC %md
# MAGIC ### **Classes - OOP**

# COMMAND ----------

class windows:

  def dense_rank(self,df):

    df_dense_rank = df.withColumn("flag",dense_rank().over(Window.partitionBy("year").orderBy(desc("total_amount"))))

    return df_dense_rank


# MAGIC %md
# MAGIC ### **Data Writing**

# COMMAND ----------

df.write.format("delta").mode("overwrite").save("abfss://silver@databricksete.dfs.core.windows.net/orders")

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS databricks_cata.silver.orders_silver
# MAGIC USING DELTA 
# MAGIC LOCATION 'abfss://silver@databricksete.dfs.core.windows.net/orders'

# COMMAND ----------

