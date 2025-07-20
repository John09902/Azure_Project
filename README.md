# 📦 Azure Databricks Lakehouse Project (Delta Live Tables)

## 🧠 Project Title
**Azure Databricks End-to-End Lakehouse with Delta Live Tables (Real-Time Retail Pipeline)**

## 🧾 One-Line Summary (for LinkedIn / CV)
> Built a real-time Lakehouse architecture using Azure Databricks, Delta Live Tables, and Unity Catalog to ingest, transform, and serve streaming retail data in a Medallion architecture.

---

## 🚀 Key Technologies
- **Cloud**: Microsoft Azure (Free Tier)
- **Data Platform**: Azure Databricks
- **Storage**: Azure Data Lake Gen2
- **Processing Engine**: PySpark + Delta Live Tables (DLT)
- **Data Governance**: Unity Catalog + Azure Key Vault
- **Orchestration**: Databricks Workflows

---

## 🧩 Project Workflow Summary
1. **Source Data**: Retail Parquet files (orders, customers, products, regions) from GitHub
2. **Ingestion Layer (Bronze)**: Loaded raw Parquet into ADLS using Structured Streaming
3. **Cleaned Layer (Silver)**: 
   - Type casting, deduplication
   - Handling nulls
   - Basic joins
4. **Business Layer (Gold)**:
   - Built Star Schema from Orders, Customers, and Products
   - Created fact table (sales) and dimension tables
   - Aggregated metrics for BI consumption
5. **SCD Type 1 & 2 Handling**:
   - Handled slowly changing dimensions using PySpark & DLT
6. **Security and Catalog**:
   - Setup Unity Catalog & External Locations
   - Managed secrets in Azure Key Vault
