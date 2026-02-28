from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime
from docker.types import Mount
import pendulum

local_tz = pendulum.timezone("Asia/Manila")

with DAG(
  dag_id="append_stocks",
    description="Daily append of stock prices at 9:00 PM Philippine time",
    schedule="0 14 * * 2-6",  # 21:00 PHT = 9 PM PH time, weekdays only
    start_date=datetime(2026, 2, 26, 21, 0, tzinfo=local_tz),  # Start at Feb 27, 2026, 9 PM PH time
    catchup=False,
    tags=["stocks"],
) as dag:

    append_stocks = DockerOperator(
    task_id="append_stocks",
    image="newfolder-loader",
    command="python append_stocks.py",
    network_mode="newfolder_stocks_net",
    environment={
        "DB_HOST": "stocks_postgres",
        "DB_PORT": "5432",
        "DB_NAME": "stocksdb",
        "DB_USER": "stocksuser",
        "DB_PASS": "stockspass",
    },
    auto_remove="success",
    docker_url="unix://var/run/docker.sock",
    )

    append_indicators = DockerOperator(
        task_id="append_indicators",
        image="newfolder-loader",
        command="python append_indicators.py",
        network_mode="newfolder_stocks_net",
        environment={
            "DB_HOST": "stocks_postgres",
            "DB_PORT": "5432",
            "DB_NAME": "stocksdb",
            "DB_USER": "stocksuser",
            "DB_PASS": "stockspass",
        },
        auto_remove="success",
        docker_url="unix://var/run/docker.sock",
    )

    append_signals = DockerOperator(
        task_id="append_signals",
        image="newfolder-loader",
        command="python append_signals.py",
        network_mode="newfolder_stocks_net",
        environment={
            "DB_HOST": "stocks_postgres",
            "DB_PORT": "5432",
            "DB_NAME": "stocksdb",
            "DB_USER": "stocksuser",
            "DB_PASS": "stockspass",
        },
        auto_remove="success",
        docker_url="unix://var/run/docker.sock",
    )

    append_stocks >> append_indicators >> append_signals