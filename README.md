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

## Project Workflow / Process

1. Extract Data

- Used Python and the yfinance library to download historical stock price data from Yahoo Finance.

- Stored the raw data in a Stock Price table, which serves as the foundation for further calculations.

2. Transform Data

- Computed technical indicators:

- MA20 (20-day moving average)

- MA50 (50-day moving average)

- RSI (Relative Strength Index)

- Stored these results in a separate Indicator table.

- Used Python with Spark (PySpark) for efficient computation on larger datasets.

3. Load Data

- Loaded the processed data into PostgreSQL.

- Created a Transaction table to log all buy/sell actions, simulating a trading workflow.

4. Automation & Orchestration

- Used Apache Airflow to automate the pipeline, scheduling daily runs.

- Pipeline organized as DAGs:

1. Extract → Stock Price Table

2. Transform → Indicator Table

3. Load → PostgreSQL / Transaction Table

5. Skills Demonstrated

- End-to-end ETL pipeline development

- Automation with Airflow DAGs

- Handling and transforming financial data using Python and Spark

- Database management in PostgreSQL

- Logging and tracking simulated transactions
