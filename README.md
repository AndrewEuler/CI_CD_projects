## CI/CD

Проект реализует REST API на Flask для инференса обученной ML-модели (Titanic classification).
Настроен простой CI/CD пайплайн с использованием GitHub Actions.

Pipeline автоматически:

- запускает автотесты (pytest)
- проверяет загрузку модели
- проверяет работу API
- собирает Docker-образ
- показывает статус выполнения

В репозитории настроен GitHub Actions pipeline:

- **Tests (pytest)** — проверка загрузки модели и API
- **Docker build** — сборка Docker-образа при push/PR

### Локальный запуск проекта
## Клонирование репозитория
```bash
git clone <repository_url>
cd CI_CD_projects
```
## Установка зависимостей
```bash
pip install -r CI_CD/requirements.txt
```
## Запуск API
```bash
python CI_CD/app.py
```
Сервис будет доступен по адресу:
```arduino
http://localhost:5000
```
## Локальный запуск тестов
```bash
pytest -q
```
