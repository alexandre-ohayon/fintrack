FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/
ENV FLASK_APP=app/__init__.py

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
