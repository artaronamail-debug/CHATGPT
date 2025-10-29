FROM python:3.11-slim

WORKDIR /app

# Pasar la variable de entorno al contenedor
ENV GEMINI_API_KEYS=$GEMINI_API_KEYS

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]