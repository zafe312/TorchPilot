FROM python:3.11-slim

WORKDIR /app

# Copy requirements from root
COPY requirements.txt .

# Copy backend source files
COPY backend/ .

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
