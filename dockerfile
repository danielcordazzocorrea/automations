FROM python:3.11-slim

WORKDIR /app

# Copia PRIMEIRO só o requirements.txt
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Depois copia o restante do projeto
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]