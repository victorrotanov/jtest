# Используем официальный образ Python 3.12
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости (копируем только requirements.txt, чтобы кешировать слои)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Создаём папку для базы данных и статических файлов
RUN mkdir -p /app/static /app/media /app/data

# Открываем порт
EXPOSE 8000

RUN python manage.py migrate && \
    echo "from django.contrib.auth import get_user_model; \
    User = get_user_model(); \
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')" \
    | python manage.py shell


# Команда для продакшена: миграции, сборка статики и запуск gunicorn
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn energy.wsgi:application --bind 0.0.0.0:8000"]
