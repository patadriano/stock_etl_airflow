# Stock ETL Pipeline with Airflow
## Overview
This project demonstrates an end-to-end data pipeline that:
- Extracts historical stock price data from Yahoo Finance for popular US stocks
- Computes technical indicators (MA20, MA50, RSI) and generates buy/sell signals
- Evaluates which indicator/strategy yields the highest simulated profit
- Loads the data into PostgreSQL and automates the pipeline using Apache Airflow

This project showcases data engineering skills: **ETL, automation, and workflow management**.

---
## Tech Stack
- Python (yfinance, pandas, sqlalchemy, psycopg2-binary)
- PostgreSQL
- Apache Airflow
- Docker
- Power BI

---
## Project Workflow / Process
1. Extract Data
  - Used Python and the yfinance library to download historical stock price data for popular US stocks (e.g. Apple, Microsoft, Tesla).
  - Stored the raw data in a Stock Price table, which serves as the foundation for further calculations.

2. Transform Data
  - Computed technical indicators using Python and Pandas:
    - MA20 (20-day moving average)
    - MA50 (50-day moving average)
    - RSI (Relative Strength Index)
  - Generated buy/sell signals based on each indicator.
  - Stored results in separate Indicator and Signal tables.

3. Load Data
  - Loaded the processed data into PostgreSQL.
  - Logged all simulated buy/sell transactions in a Transaction table to track performance per strategy.

4. Automation & Orchestration
  - Used Apache Airflow to automate the daily extraction of stock data and schedule pipeline runs.
  - Pipeline organized as DAGs:
    1. Extract → pulls raw stock data from Yahoo Finance → stores in Stock Price table
    2. Transform → reads Stock Price table → computes indicators (MA20, MA50, RSI) → stores in Indicator table
    3. Load → reads Indicator table → generates buy/sell signals and computes simulated profit → stores in Transaction table

5. Analysis & Visualization
  - Connected PostgreSQL to Power BI to visualize and compare indicator performance.
  - Dashboard highlights which indicator/strategy generates the most profit across different stocks.
  - Stock price trends are also displayed alongside signals for better context.

6. Docker
  - Used Docker and Docker Compose for easy setup and to run Apache Airflow in containers, ensuring a consistent environment.

7. Skills Demonstrated
  - End-to-end ETL pipeline development
  - Automation with Airflow DAGs
  - Financial data transformation using Python and Pandas
  - Strategy backtesting and performance comparison
  - Database management in PostgreSQL
  - Data visualization with Power BI
  - Containerization with Docker
