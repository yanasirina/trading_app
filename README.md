# Trading App

### Запуск контейнеров:
docker run -p 5433:5432 --name pg_trading -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -d postgres:16.0 \
docker run -d --restart always -p 6379:6379 --name=redis redis

### Создать первоначальные миграции:
alembic init migrations

### Создание и прогон миграций
alembic revision --autogenerate -m "название_миграции" \
alembic upgrade хэш_миграции

### Запуск celery + flower
celery -A celery_worker:celery_app worker --loglevel=INFO \
celery -A celery_worker:celery_app flower --loglevel=INFO