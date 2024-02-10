# Trading App

### Запуск БД:
docker run -p 5433:5432 --name pg_trading -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -d postgres:16.0

### Создать первоначальные миграции:
alembic init migrations

### Создание и прогон миграций
alembic revision --autogenerate -m "название_миграции" \
alembic upgrade хэш_миграции
