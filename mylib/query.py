from pyspark.sql import SparkSession

# Initialize Spark session if it's not already initialized
spark = SparkSession.builder \
    .appName("Spark App") \
    .config("spark.jars.packages", "io.delta:delta-core_2.12:1.2.1") \
    .getOrCreate()
    
# Markdown file to log the SQL functions and queries
def logQuery(query):
    with open("queryLog.md", "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")

# Register the Delta table as a temporary view
delta_table_path = "dbfs:/FileStore/nmc58_mini_project11/nmc58_mini_project11_delta_table"
spark.read.format("delta").load(delta_table_path).createOrReplaceTempView("nmc58_mini_project11_delta_table")

# Now you can run SQL queries on the registered table
def query():
    query = """
        SELECT *
        FROM nmc58_mini_project11_delta_table
        WHERE number_of_subjects = 4
        """
    # Log the query
    logQuery(query)
    query_result = spark.sql(query)
    query_result.show()