# Banco de dados

Este é o serviço **database** desenvolvido em **Docker Compose**.
Ele fornece o banco de dados PostgreSQL para o backend.

---

## 📦 Requisitos

* **Docker & Docker Compose** (apenas para o banco de dados)

---

## ▶️ Rodando o banco de dados

### 2. Configurar variáveis de ambiente

O projeto utiliza variáveis de ambiente para configurar itens como a conexão com o banco.

Na raiz do projeto existe um arquivo `.env.example`.
Você deve copiá-lo para `.env` e ajustar os valores conforme sua necessidade:

```bash
cp .env.example .env
```

---

### 1. Subir o banco de dados

Antes de iniciar o backend, é necessário subir o banco.
Na pasta `database`, execute:

```bash
docker compose up -d
```

Isso irá iniciar o banco de dados em contêiner.


