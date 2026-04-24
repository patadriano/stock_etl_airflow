# Stock ETL Pipeline with Airflow

## Overview

This project demonstrates an end-to-end data pipeline that:

- Extracts historical stock price data from Yahoo Finance for popular US stocks  
- Computes technical indicators (MA20, MA50, RSI) and generates buy/sell signals based on MA Cross and RSI strategies  
- Evaluates which strategy yields the highest simulated profit  
- Loads the data into PostgreSQL and automates the pipeline using Apache Airflow  

This project showcases data engineering skills: ETL, automation, and workflow management.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python (yfinance, pandas, sqlalchemy, psycopg2-binary) | Data extraction & transformation |
| PostgreSQL | Data storage |
| Apache Airflow | Pipeline orchestration |
| Docker | Containerization |
| Power BI | Data visualization |

---

## Project Workflow

### 1. Extract Data
- Used Python and the yfinance library to download historical stock price data for:
  - AAPL (Apple)
  - MSFT (Microsoft)
  - GOOGL (Google)
  - NVDA (Nvidia)
  - AMZN (Amazon)

- Stored raw data in a `stock_price` table.

---

### 2. Transform Data
- Computed technical indicators:
  - MA20 (20-day moving average)
  - MA50 (50-day moving average)
  - RSI (Relative Strength Index)

- Generated buy/sell signals:
  - **MA_CROSS**  
    - Buy: MA20 crosses above MA50  
    - Sell: MA20 crosses below MA50  

  - **RSI**  
    - Buy: RSI < 30 (oversold)  
    - Sell: RSI > 70 (overbought)

- Stored results in:
  - `indicator` table  
  - `signal` table  

---

### 3. Load Data
- Loaded processed data into PostgreSQL  
- Logged simulated trades in a `transaction` table for performance tracking  

---

### 4. Automation (Airflow DAGs)
