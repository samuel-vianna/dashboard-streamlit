#!/bin/bash
set -e

# Rodar servidor FastAPI
echo "🚀 Iniciando backend..."
uvicorn main:app --host 0.0.0.0 --port 8000 --reload


# Rodar seeds
echo "🛠 Rodando seeds..."
python scripts/seed.py
python scripts/seed_feedback.py
