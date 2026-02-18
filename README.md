## CI/CD

В репозитории настроен GitHub Actions pipeline:

- **Tests (pytest)** — проверка загрузки модели и API
- **Docker build** — сборка Docker-образа при push/PR

### Локальный запуск тестов
```bash
pip install -r requirements.txt
pytest -q