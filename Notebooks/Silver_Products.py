# Databricks notebook source
from pyspark.sql.functions import * 
from pyspark.sql.types import * 

# COMMAND ----------

# MAGIC %md
# MAGIC ### **Data Reading**

# COMMAND ----------

df = spark.read.format("parquet")\
          .load("abfss://bronze@databricksete.dfs.core.windows.net/products")

# COMMAND ----------

df.display()

# COMMAND ----------

df = df.drop("_rescued_data")

# COMMAND ----------

df.createOrReplaceTempView("products")

# COMMAND ----------

# MAGIC %md
# MAGIC ### **Functions**

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE FUNCTION databricks_cata.bronze.discount_func(p_price DOUBLE) 
# MAGIC RETURNS DOUBLE  
# MAGIC LANGUAGE SQL 
# MAGIC RETURN p_price * 0.90

# COMMAND ----------

df = df.withColumn("discounted_price",expr("databricks_cata.bronze.discount_func(price)"))
df.display()

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE FUNCTION databricks_cata.bronze.upper_func(p_brand STRING)
# MAGIC RETURNS STRING 
# MAGIC LANGUAGE PYTHON 
# MAGIC AS 
# MAGIC $$ 
# MAGIC     return p_brand.upper()
# MAGIC $$

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT product_id, brand, databricks_cata.bronze.upper_func(brand) as brand_upper
# MAGIC FROM products

# COMMAND ----------

df.write.format("delta")\
            .mode("overwrite")\
            .option("path","abfss://silver@databricksete.dfs.core.windows.net/products")\
            .save()

# COMMAND ----------


