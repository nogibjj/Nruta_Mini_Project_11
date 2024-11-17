# Databricks notebook source
%pip install python-dotenv

# COMMAND ----------

# MAGIC %restart_python

# COMMAND ----------

from mylib.extract import extract

# COMMAND ----------

extract()

# COMMAND ----------

from mylib.transform_load import transform_data

# COMMAND ----------

# Define paths
delta_table_path = "dbfs:/FileStore/nmc58_mini_project11/nmc58_mini_project11_delta_table"
dbfs_file_path = "dbfs:/FileStore/nmc58_mini_project11/biopics.csv"

transform_data(dbfs_file_path)

