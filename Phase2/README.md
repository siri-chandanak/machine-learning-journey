# Core Machine Learning & Data Engineering

This phase focuses on building solid foundations in Machine Learning and Data Engineering.
You’ll learn how to preprocess, train, evaluate, and deploy ML models while understanding how data flows through pipelines and large-scale systems.

## Machine Learning (Scikit-learn)
1. Supervised ML
    - Linear Regression -- Linear_Regression.ipynb
    - Logistic Regression classification -- Logistic_Regression.ipynb
    - Decision Trees & Random Forests -- Decision_Trees_Random_Forests.ipynb
2. Unsupervised ML
    - Clustering (K-Means, Hierarchical) -- Clustering.ipynb
    - Dimensionality Reduction (PCA) -- PCA.ipynb
3. Model Evaluation Metrics -- Model_Evaluation.ipynb
    - Accuracy, Precision, Recall
    - ROC Curve, AUC
    - Cross-validation and Hyperparameter Tuning

## Deep Learning (TensorFlow / PyTorch)
1. Artificial Neural Networks (ANN) -- ANN.ipynb
    - Forward pass, Backpropagation
2. Convolutional Neural Networks (CNN) -- CNN.ipynb
    - Image classification basics
    - Convolutional layers, Pooling layers
    - Transfer learning with pre-trained models
3. Recurrent Neural Networks (RNN) & LSTM -- RNN_LSTM.ipynb
    - Sequence data handling    
    - Time series forecasting
4. Transfer Learning -- Transfer_Learning.ipynb
    - Using models like ResNet, VGG, InceptionNet for custom tasks

## Data Engineering Essentials
1. ETL Pipelines - ETL_Airflow_Pipeline.ipynb
    - Basics of ETL (Extract, Transform, Load)
    - Tools: Apache Airflow, AWS Glue basics
2. Big Data Tools
    - Apache Spark (PySpark basics) -- PySpark.ipynb
    - Hadoop
3. Data Warehousing -- Data_Warehouse_Design.ipynb
    - Concepts: OLAP vs OLTP
    - Tools: Amazon Redshift, Google BigQuery Snowflake
    - Schema design: Star vs Snowflake schema

# 📂 Data Engineering Tools & Concepts

This section covers **core data engineering tools and concepts** essential for building robust ETL pipelines, handling big data, and designing analytical databases.  

---

## **Apache Airflow**
**Purpose:** Workflow orchestration tool to automate ETL and data pipelines.  

### Key Concepts:
- **DAG (Directed Acyclic Graph):** Represents the pipeline.  
- **Task:** Individual step in a DAG.  
- **Operators:** Define what each task does (`PythonOperator`, `BashOperator`, `SparkSubmitOperator`).  
- **Scheduler:** Executes DAGs at defined intervals.  
- **XComs:** Enable communication between tasks.  

### Hands-on Ideas:
- Create a DAG to **extract data from CSV → transform → load to database**.  
- Schedule it daily and log task execution.  

### References:
- [Airflow Documentation](https://airflow.apache.org/docs/)

---

## **AWS Glue Basics**
**Purpose:** Fully managed ETL service for preparing and loading data.  

### Key Concepts:
- **Crawler:** Automatically discovers schema and metadata.  
- **ETL Jobs:** Scripts to transform and move data.  
- **Data Catalog:** Stores table definitions for easy query.  
- **Triggers:** Automate ETL job execution.  

### Hands-on Ideas:
- Create a Glue job to **clean CSV data and load it to S3 or Redshift**.  
- Schedule Glue jobs using triggers or Airflow integration.  

### References:
- [AWS Glue Documentation](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html)

---

## **Hadoop**
**Purpose:** Distributed storage and processing of massive datasets.  

### Key Concepts:
- **HDFS (Hadoop Distributed File System):** Stores files across multiple nodes.  
- **MapReduce:** Parallel processing model (Map → Shuffle → Reduce).  
- **YARN:** Resource management and job scheduling.  

### Hands-on Ideas:
- Install Hadoop pseudo-distributed mode.  
- Write a MapReduce job to **count word frequency** in large text files.  

### References:
- [Hadoop Documentation](https://hadoop.apache.org/docs/stable/)

---

## **Data Warehousing**
**Purpose:** Optimized for analytical queries on large datasets.  

### Tools:
- **Amazon Redshift**: Cloud data warehouse, fast SQL analytics.  
- **Google BigQuery**: Serverless, highly scalable analytics.  
- **Snowflake**: Cloud data warehouse supporting structured and semi-structured data.  

### Concepts:
- **OLAP vs OLTP:**  
  - OLTP: Transactional systems (high insert/update throughput)  
  - OLAP: Analytical systems (aggregates, reporting, large queries)  

- **Schema Design:**  
  - **Star Schema:** Central fact table connected to dimension tables  
    - Simple queries, denormalized  
  - **Snowflake Schema:** Normalized dimension tables  
    - Reduces redundancy, more complex joins  

### Hands-on Ideas:
- Design a **Star Schema** for retail sales:  
  - Fact table: `sales` (transaction_id, product_id, store_id, date, quantity, revenue)  
  - Dimension tables: `products`, `stores`, `customers`, `time`  
- Run aggregation queries: total sales per product or store.  

### References:
- [Redshift Documentation](https://docs.aws.amazon.com/redshift/latest/dg/welcome.html)  
- [BigQuery Documentation](https://cloud.google.com/bigquery/docs)  
- [Snowflake Documentation](https://docs.snowflake.com/)

---

## ✅ Outcome
By understanding and practicing these tools, you will be able to:
- Automate ETL pipelines using Airflow & AWS Glue  
- Process and analyze large datasets with Hadoop  
- Design optimized schemas for data warehouses  
- Run analytical queries efficiently on cloud warehouses (Redshift, BigQuery, Snowflake)
