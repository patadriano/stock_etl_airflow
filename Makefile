.PHONY: up down restart psql reserialize \
        trigger-manual trigger-append \
        run-load run-indicators run-signals \
        build check check-scheduler logs-scheduler logs-webserver

# ── Startup & Shutdown ───────────────────────────────────────────────────────

## Full stack startup: postgres → airflow infra → webserver + scheduler
up:
	docker compose up -d postgres airflow-db airflow-init
	@echo "Waiting 30s for airflow-init to finish..."
	sleep 30
	docker compose up -d airflow-webserver airflow-scheduler
	docker exec -it airflow_scheduler airflow dags reserialize

## Stop all containers (keeps data volumes)
down:
	docker compose down

## Stop everything including data volumes (full reset)
down-v:
	docker compose down -v

## Restart the full stack
restart: down up

# ── Database ─────────────────────────────────────────────────────────────────

## Open a psql shell into the stocks database
psql:
	docker exec -it stocks_postgres psql -U $${STOCKS_USER} -d $${STOCKS_DB}

# ── Airflow DAG Management ───────────────────────────────────────────────────

## Reserialize all DAGs (run after editing any DAG file)
reserialize:
	docker exec -it airflow_scheduler airflow dags reserialize

## Manually trigger the manual_pipeline DAG
trigger-manual:
	docker exec -it airflow_scheduler airflow dags trigger manual_pipeline

## Manually trigger the append_stocks DAG
trigger-append:
	docker exec -it airflow_scheduler airflow dags trigger append_stocks

# ── Manual Python Scripts ────────────────────────────────────────────────────

## Run load_stocks.py manually
run-load:
	docker compose run --rm loader python load_stocks.py

## Run compute_indicators.py manually
run-indicators:
	docker compose run --rm loader python compute_indicators.py

## Run generate_signals.py manually
run-signals:
	docker compose run --rm loader python generate_signals.py

# ── Build ────────────────────────────────────────────────────────────────────

## Rebuild the loader image
build:
	docker compose build loader

# ── Health Checks & Logs ─────────────────────────────────────────────────────

## Show all running containers
check:
	docker ps

## Check if the Airflow scheduler is alive
check-scheduler:
	docker exec -it airflow_scheduler airflow jobs check

## Tail scheduler logs
logs-scheduler:
	docker logs -f airflow_scheduler

## Tail webserver logs
logs-webserver:
	docker logs -f airflow_webserver