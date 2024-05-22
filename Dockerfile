FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

<<<<<<< HEAD
ENV DJANGO_SETTINGS_MODULE=streets_backend.settings
=======
ENV DJANGO_SETTINGS_MODULE=streets_backend.streets_backend.settings
>>>>>>> 47dd3a8 (Настройка workflows для деплоя на сервер.)

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "streets_backend.wsgi"]