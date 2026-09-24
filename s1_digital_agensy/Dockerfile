# Используем легковесный образ Python, оптимизированный под архитектуру ARM (для Mac)
FROM python:3.12-slim

# Устанавливаем переменные окружения, чтобы Python не создавал файлы .pyc и выдавал логи без задержек
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Создаем и переходим в рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt /app/

# Обновляем pip и устанавливаем зависимости
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Копируем весь остальной код проекта в контейнер
COPY . /app/

# Команда по умолчанию для запуска сервера разработки Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

