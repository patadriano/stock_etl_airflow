# Setup & Development Guide

## Project Structure
```
your-project/
│
├── .env                    ← your secrets (never commit)
├── .env.example            ← blank template (commit this)
├── .gitignore
├── Makefile
├── Dockerfile
├── requirements.txt
├── docker-compose.yml
│
├── README.md               ← employer-facing (project overview)
│
├── docs/
│   └── SETUP.md            ← this file
│
├── scripts/
│   └── queries.sql         ← debug / validation queries
│
├── app/
│   ├── load_stocks.py
│   ├── compute_indicators.py
│   ├── generate_signals.py
│   ├── append_stocks.py
│   ├── append_indicators.py
│   └── append_signals.py
│
└── dags/
    └── your_dag_files.py
```

---

## Prerequisites

### Installing `make`

`make` is required to run the Makefile commands. Docker Desktop must also be installed on your machine.

**Windows:**
Install via Chocolatey (run in Command Prompt as Administrator):
```cmd
choco install make
```
Or use **Git Bash** — it comes with `make` built in and is the easiest option on Windows.

**Mac:**
```bash
xcode-select --install
```

---

## First-Time Setup

### 1. Create your `.env` file

**Windows (Command Prompt):**
```cmd
copy .env.example .env
```

**Mac/Linux:**
```bash
cp .env.example .env
```

Then open `.env` and fill in your values. It is pre-filled with working defaults — change them if you want stronger credentials.

> `.env` is in `.gitignore` and will never be committed to GitHub.

---

### 2. Build the loader image

**Windows & Mac:**
```
make build
```

---

### 3. Start the full stack

**Windows & Mac:**
```
make up
```

This starts PostgreSQL, initializes Airflow, then brings up the webserver and scheduler.
Airflow UI will be available at **http://localhost:8080** (login: `admin` / `admin`).

---

## Common Commands

All commands are run as `make <command>` in your terminal from the project root.

| Command | What it does |
|---|---|
| `make up` | Start the full stack |
| `make down` | Stop all containers (keeps data) |
| `make down-v` | Stop + delete all data volumes (full reset) |
| `make restart` | Full down → up cycle |
| `make build` | Rebuild the loader image |
| `make psql` | Open psql shell into the stocks database |
| `make reserialize` | Reload DAGs after editing a DAG file |
| `make trigger-manual` | Trigger the `manual_pipeline` DAG |
| `make trigger-append` | Trigger the `append_stocks` DAG |
| `make run-load` | Run `load_stocks.py` manually |
| `make run-indicators` | Run `compute_indicators.py` manually |
| `make run-signals` | Run `generate_signals.py` manually |
| `make check` | List all running containers |
| `make check-scheduler` | Check Airflow scheduler health |
| `make logs-scheduler` | Tail scheduler logs |
| `make logs-webserver` | Tail webserver logs |

---

## Connecting to PostgreSQL

**From your host machine:**

Windows (Command Prompt):
```cmd
psql -h localhost -p 5432 -U stocksuser -d stocksdb
```

Mac/Linux:
```bash
psql -h localhost -p 5432 -U stocksuser -d stocksdb
```

**Inside Docker (via Makefile — same on both OS):**
```
make psql
```

---

## Re-running the Loader

The script uses `if_exists="append"` so it adds rows on each run.
To replace data instead, change this line in `load_stocks.py`:

```python
# Change:
if_exists="append"
# To:
if_exists="replace"
```

---

## Stop Everything

```
make down      # Stop containers, keep data
make down-v    # Stop containers, delete all data
```