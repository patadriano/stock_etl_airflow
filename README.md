# Stock ETL Pipeline with Airflow

## Overview
This project demonstrates an end-to-end data pipeline that:
- Extracts stock price data from Yahoo Finance
- Cleans and transforms the data (moving averages: MA20, MA50 and RSI)
- Loads the data into PostgreSQL
- Automates the pipeline using Apache Airflow

This project showcases data engineering skills: **ETL, automation, and workflow management**.

---

## Tech Stack
- Python 3.9
- Pandas
- PostgreSQL
- Apache Airflow
- yfinance

---

Project Workflow / Process

Extract Data

Used Python and the yfinance library to download historical stock price data from Yahoo Finance.

Stored the raw data in a Stock Price table, which serves as the foundation for further calculations.

Transform Data

Computed technical indicators:

MA20 (20-day moving average)

MA50 (50-day moving average)

RSI (Relative Strength Index)

These calculations were stored in a separate Indicator table for clarity and reusability.

Used Python with Spark (PySpark) to handle transformations efficiently for larger datasets.

Load Data

Loaded the processed data into PostgreSQL, ensuring tables were structured for efficient querying.

Maintained a Transaction table to log all buy/sell actions, simulating a trading workflow.

Automation & Orchestration

Used Apache Airflow to automate the pipeline, scheduling daily runs.

Tasks were organized as DAGs:

Extract → Stock Price Table

Transform → Indicator Table

Load → PostgreSQL / Transaction Table

Skills Demonstrated

End-to-end ETL pipeline development

Automation with Airflow DAGs

Handling and transforming financial data using Python and Spark

Database management in PostgreSQL

Logging and tracking simulated transactions

