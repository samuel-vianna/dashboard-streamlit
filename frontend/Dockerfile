# Usar imagem base do Python
FROM python:3.13-slim

# Definir diretório de trabalho
WORKDIR /app

# Copiar requirements e instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o código do frontend
COPY ./src /app/src
COPY .env /app/.env

# Expor porta do Streamlit
EXPOSE 8500

# Comando para rodar o Streamlit
CMD ["streamlit", "run", "src/main.py", "--server.port=8500", "--server.address=0.0.0.0"]
