# Вибір базового образу
FROM python:3.10-slim
LABEL authors="Spedy"

# Встановлення робочої директорії у контейнері
WORKDIR /app

# Копіювання вашого Python-скрипту та інших необхідних файлів
COPY . /app

# Запуск вашого Python-скрипту
CMD ["python", "main.py"]