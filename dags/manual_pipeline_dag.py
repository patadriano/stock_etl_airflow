from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime
import pendulum

local_tz = pendulum.timezone("Asia/Manila")

with DAG(
    dag_id="manual_pipeline",
    description="Manually triggered: load_stocks -> compute_indicators -> generate_signals",
    schedule=None,  # manual trigger only
    start_date=datetime(2026, 1, 1, tzinfo=local_tz),
    catchup=False,
    tags=["stocks", "manual"],
) as dag:

    load_stocks = DockerOperator(
        task_id="load_stocks",
        image="newfolder-loader",
        command="python load_stocks.py",
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

    compute_indicators = DockerOperator(
        task_id="compute_indicators",
        image="newfolder-loader",
        command="python compute_indicators.py",
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

    generate_signals = DockerOperator(
        task_id="generate_signals",
        image="newfolder-loader",
        command="python generate_signals.py",
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

    load_stocks >> compute_indicators >> generate_signals