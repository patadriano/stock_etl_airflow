# Stock Prices Loader — Docker + PostgreSQL

## Project Structure
```
.
├── docker-compose.yml   # PostgreSQL service + loader service definition
├── Dockerfile           # Python image for the loader
├── load_stocks.py       # The ETL script (yfinance → PostgreSQL)
├── requirements.txt     # Python dependencies
└── README.md
```

---

## 1. Start PostgreSQL

```bash
docker compose up -d postgres
```

This starts a PostgreSQL 16 container with:
- **Database:** `stocksdb`
- **User:** `stocksuser`
- **Password:** `stockspass`
- **Port:** `5432` (exposed to host)

---

## 2. Build the loader image

```bash
docker compose build loader
```

---

## 3. Run the script manually (whenever you want)

```bash
docker compose run --rm loader
```

This runs `load_stocks.py` inside a container that is connected to the
`stocks_postgres` container via Docker's internal network.

### Re-running

The script uses `if_exists="append"` so it will **add** rows on each run.
If you want to **replace** the data instead, change line in `load_stocks.py`:
```python
# Change:
if_exists="append"
# To:
if_exists="replace"
```

---

## 4. Connect to PostgreSQL to verify

**From host machine:**
```bash
psql -h localhost -p 5432 -U stocksuser -d stocksdb
```

**Inside Docker:**
```bash
docker exec -it stocks_postgres psql -U stocksuser -d stocksdb
```

**Sample queries:**
```sql
-- Row count
SELECT ticker, COUNT(*) FROM stock_prices GROUP BY ticker;

-- Latest prices
SELECT * FROM stock_prices ORDER BY date DESC LIMIT 10;

-- Date range
SELECT MIN(date), MAX(date) FROM stock_prices;
```

---

## 5. Stop everything

```bash
docker compose down          # stop containers (keeps data volume)
docker compose down -v       # stop + delete all data
```

---

## Environment Variables

The script reads connection settings from env vars (set in `docker-compose.yml`).
You can override them when running manually:

```bash
DB_HOST=localhost DB_PORT=5432 python load_stocks.py
```
