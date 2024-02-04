# Trading App

### Запуск БД:
docker run -p 5433:5432 --name pg_trading -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -d postgres:16.0
