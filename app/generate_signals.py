import pandas as pd
from sqlalchemy import create_engine, text
import os

# --- Config ---
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "stocksdb")
DB_USER = os.getenv("DB_USER", "stocksuser")
DB_PASS = os.getenv("DB_PASS", "stockspass")

tickers = ["NVDA", "AAPL", "MSFT", "GOOGL", "AMZN"]

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

print("=" * 50)
print("Generating trading signals...")
print("=" * 50)

# ─────────────────────────────────────────────
# Create transactions table if not exists
# ─────────────────────────────────────────────
with engine.begin() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS transactions (
            date        DATE,
            ticker      VARCHAR(10),
            value       NUMERIC,
            signal      VARCHAR(10),
            strategy    VARCHAR(20),
            PRIMARY KEY (date, ticker, strategy)
        )
    """))

# ─────────────────────────────────────────────
# Signal generation function
# ─────────────────────────────────────────────
def generate_signals(pdf: pd.DataFrame) -> pd.DataFrame:
    pdf = pdf.sort_values("date").reset_index(drop=True)
    out = []

    # ===== RSI Strategy =====
    last_signal = None
    for _, r in pdf.iterrows():
        rsi = r["rsi_14"]
        if pd.isna(rsi):
            continue

        signal = None
        if rsi < 30 and last_signal != "BUY":
            signal = "BUY"
            last_signal = "BUY"
        elif rsi > 70 and last_signal == "BUY":
            signal = "SELL"
            last_signal = "SELL"

        if signal:
            out.append({
                "date":     r["date"],
                "ticker":   r["ticker"],
                "value":    round(float(rsi), 4),
                "signal":   signal,
                "strategy": "RSI"
            })

    # ===== MA Crossover Strategy =====
    # Requires both ma_20 and ma_50; signal when MA20 crosses MA50
    last_ma_signal = None
    for i, r in pdf.iterrows():
        ma20 = r["ma_20"]
        ma50 = r["ma_50"]
        if pd.isna(ma20) or pd.isna(ma50):
            continue

        signal = None
        if ma20 > ma50 and last_ma_signal != "BUY":
            signal = "BUY"
            last_ma_signal = "BUY"
        elif ma20 < ma50 and last_ma_signal == "BUY":
            signal = "SELL"
            last_ma_signal = "SELL"

        if signal:
            out.append({
                "date":     r["date"],
                "ticker":   r["ticker"],
                "value":    round(float(ma20), 4),
                "signal":   signal,
                "strategy": "MA_CROSS"
            })

    return pd.DataFrame(out, columns=["date", "ticker", "value", "signal", "strategy"])


# ─────────────────────────────────────────────
# Loop over tickers
# ─────────────────────────────────────────────
total_signals = 0

for ticker in tickers:
    print(f"\nProcessing {ticker}...")

    pdf = pd.read_sql(
        f"SELECT * FROM stock_indicators WHERE ticker = '{ticker}' ORDER BY date",
        engine
    )

    if pdf.empty:
        print(f"  ⚠️  No indicator data for {ticker}. Run compute_indicators.py first.")
        continue

    signals_df = generate_signals(pdf)

    if signals_df.empty:
        print(f"  No signals generated for {ticker}.")
        continue

    signals_df.to_sql(
        "transactions",
        engine,
        if_exists="append",
        index=False,
        method="multi",
        chunksize=500
    )

    count = len(signals_df)
    total_signals += count
    print(f"  ✅ {count} signals appended.")
    print(signals_df.to_string(index=False))

print(f"\n🎉 Done! Total signals written to transactions table: {total_signals}")
