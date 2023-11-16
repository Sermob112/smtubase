# Используем официальный образ Python
FROM python:3.11
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install gunicorn && pip install -r requirements.txt
COPY . /app/
CMD ["gunicorn", "smtubase.wsgi:application", "--bind", "0.0.0.0:8000"]
