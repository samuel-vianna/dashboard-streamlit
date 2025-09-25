# Backend (FastAPI)

Instruções para instalar e testar localmente o serviço backend (FastAPI).

## Requisitos

- Docker & Docker Compose (ou Docker CLI com suporte `docker compose`)
- Python 3.11 (se for executar sem Docker)
- Git (opcional)

Arquivos relevantes:

- [docker-compose.yaml](../docker-compose.yaml)
- [Dockerfile](./Dockerfile)
- [requirements.txt](./requirements.txt)
- Código da API: [`main.app`](./app/main.py) / [`main.read_root`](./app/main.py)

## Rodar com Docker Compose

## Rodar localmente

- Criar e ativar um ambiente virtual Python

```bash
python -m venv venv
source venv/bin/activate
```

- Instalar as dependências

```bash
pip install -r requirements.txt

pip freeze > requirements.txt # copiar arquivos para dependências

```

- Rodar o servidor

```bash
fastapi dev app/main.py
```

- Testar

```bash
curl http://localhost:8000/
```
