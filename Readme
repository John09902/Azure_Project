Azure Databricks End-to-End Lakehouse Pipeline

Overview

This project implements a real-time data engineering pipeline using Azure Databricks to process retail data (Orders, Customers, Products, Regions) in a medallion architecture. It leverages Spark Structured Streaming, Delta Live Tables, and Unity Catalog to ingest, transform, and model data into a star schema, with integration to Power BI for analytics. The pipeline handles incremental loading, Type 1/2 slowly changing dimensions (SCD), and orchestrated ETL workflows.

Project Architecture





Data Source: Parquet files (Orders, Customers, Products, Regions) stored in Azure Data Lake.



Bronze Layer: Incremental ingestion using Spark Structured Streaming with idempotency.



Silver Layer: Data transformations using PySpark and Python OOP, stored in Delta format.



Gold Layer: Star schema with dimension (dim_customers, dim_products) and fact (fact_orders) tables, implementing SCD Type 1 (manual) and Type 2 (via Delta Live Tables).



Orchestration: Databricks workflows for parallel (Silver) and sequential (Gold) ETL tasks.



Output: SQL queries for validation and Power BI integration for visualizations.

Repository Structure





data/sample_data/: Sample Parquet files for Orders, Customers, Products, and Regions.



notebooks/: Databricks notebooks organized by layer:





bronze/: Parameters and incremental loading.



silver/: Transformations for Orders, Customers, Products.



gold/: Dimension/fact table creation and Delta Live Tables for SCD.



queries/: SQL queries for table validation.



screenshots/: Pipeline workflow, SQL visualizations, and Power BI connection.

Setup Instructions





Prerequisites: Azure Databricks (trial), Azure Data Lake Storage, Python 3.8+, PySpark, Delta Lake.



Clone Repository: git clone https://github.com/yourusername/Azure-Databricks-Lakehouse-Project.git



Install Dependencies: pip install -r requirements.txt



Run Notebooks: Import .py files into Databricks, configure Data Lake paths, and execute notebooks in sequence (Bronze → Silver → Gold).



View Results: Run SQL queries in queries/ or check screenshots/ for pipeline and visualization outputs.

Results





Processed 10,000+ order records with incremental updates, ensuring exactly-once semantics.



Built a star schema with SCD Type 1/2 for historical data tracking.
