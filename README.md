# 📈 Stock ETL Pipeline with Airflow

## 📌 Overview

This project demonstrates an end-to-end data pipeline that:

- 📥 Extracts historical stock price data from Yahoo Finance for popular US stocks
- 🔄 Computes technical indicators (MA20, MA50, RSI) and generates buy/sell signals based on **MA Cross** and **RSI** strategies
- 📊 Evaluates which strategy yields the highest simulated profit
- 🗄️ Loads the data into PostgreSQL and automates the pipeline using Apache Airflow

> This project showcases data engineering skills: **ETL, automation, and workflow management**.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python (yfinance, pandas, sqlalchemy, psycopg2-binary) | Data extraction & transformation |
| PostgreSQL | Data storage |
| Apache Airflow | Pipeline orchestration |
| Docker | Containerization |
| Power BI | Data visualization |

---

## 🔄 Project Workflow

### 1. 📥 Extract Data
- Used **Python** and the **yfinance** library to download historical stock price data for popular US stocks:
  - `AAPL` (Apple), `MSFT` (Microsoft), `GOOGL` (Google), `NVDA` (Nvidia), `AMZN` (Amazon)
- Stored the raw data in a **Stock Price** table, which serves as the foundation for further calculations.

---

### 2. 🔧 Transform Data
- Computed technical indicators using **Python** and **Pandas**:
  - **MA20** — 20-day moving average
  - **MA50** — 50-day moving average
  - **RSI** — Relative Strength Index
- Generated buy/sell signals based on two strategies:
  - **MA_CROSS** — a buy/sell signal is triggered when the MA20 crosses above or below the MA50
  - **RSI** — a buy signal is triggered when RSI drops below 30 (oversold); a sell signal when RSI rises above 70 (overbought)
- Stored results in separate **Indicator** and **Signal** tables.

---

### 3. 🗄️ Load Data
- Loaded the processed data into **PostgreSQL**.
- Logged all simulated buy/sell transactions in a **Transaction** table to track performance per strategy.

---

### 4. ⚙️ Automation & Orchestration
- Used **Apache Airflow** to automate the daily extraction of stock data and schedule pipeline runs.
- Pipeline organized as **DAGs**:

```
DAG 1: Extract  →  Pulls raw stock data from Yahoo Finance  →  Stores in Stock Price table
DAG 2: Transform  →  Reads Stock Price table  →  Computes indicators (MA20, MA50, RSI)  →  Stores in Indicator table
DAG 3: Load  →  Reads Indicator table  →  Generates buy/sell signals & computes simulated profit  →  Stores in Transaction table
```

---

### 5. 📊 Analysis & Visualization
- Connected **PostgreSQL** to **Power BI** to visualize and compare strategy performance.
- Dashboard highlights which strategy (**MA_CROSS** or **RSI**) generates the most profit across different stocks (AAPL, MSFT, GOOGL, NVDA, AMZN).

---

### 6. 🐳 Docker
- Used **Docker** and **Docker Compose** for easy setup and to run Apache Airflow in containers, ensuring a consistent and reproducible environment.

---

## ✅ Skills Demonstrated

- ✔️ End-to-end ETL pipeline development
- ✔️ Automation with Airflow DAGs
- ✔️ Financial data transformation using Python and Pandas
- ✔️ Strategy backtesting and performance comparison
- ✔️ Database management in PostgreSQL
- ✔️ Data visualization with Power BI
- ✔️ Containerization with Docker
