# Backend (FastAPI)

Este é o serviço **backend** desenvolvido em **FastAPI**.
Aqui estão as instruções para rodar o projeto **localmente**.

---

## 📦 Requisitos

* **Python 3.13**

Arquivos principais:

* [`docker-compose.yaml`](../docker-compose.yaml)
* [`Dockerfile`](./Dockerfile)
* [`requirements.txt`](./requirements.txt)
* API principal: [`app/main.py`](./app/main.py)

---

## ▶️ Rodando o projeto

### 1. Subir o banco de dados

Antes de iniciar o backend, é necessário subir o banco.
Na pasta `database`, execute:

```bash
cd ../database
docker compose up -d
```

Isso irá iniciar o banco de dados em contêiner.

---

### 2. Configurar variáveis de ambiente

O projeto utiliza variáveis de ambiente para configurar itens como a conexão com o banco.

Na raiz do projeto existe um arquivo `.env.example`.
Você deve copiá-lo para `.env` e ajustar os valores conforme sua necessidade:

```bash
cp .env.example .env
```

---

### 3. Rodar o backend localmente

1. Criar e ativar um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Instalar as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Subir o servidor:

   ```bash
   uvicorn app.main:app --reload
   ```

4. Testar:

   ```bash
   curl http://localhost:8000/
   ```

---

## 📂 Estrutura de Pastas

```bash
.
├── Dockerfile
├── README.md
├── app
│   ├── __init__.py
│   ├── config/          # Configurações gerais
│   ├── controllers/     # Controllers (rotas)
│   ├── main.py          # Ponto de entrada da aplicação
│   ├── models/          # Modelos do banco de dados (SQLAlchemy)
│   ├── repositories/    # Acesso a dados
│   ├── schemas/         # Schemas Pydantic (validação/serialização)
│   ├── services/        # Serviços e lógica de negócio
│   ├── usecases/        # Casos de uso específicos (funções usadas pelos controllers)
│   └── utils/      
├── scripts     # Arquivos para popular banco de dados
├── requirements.txt
├── tests/               # Testes unitários e de integração
└── venv/                # Ambiente virtual
```

## Adicionando novos modelos de LLM

Para adicionar novos modelos de LLM, siga os seguintes passos:

- Vá ao arquivo `backend/app/services/llm/llm_client.py`
- Adicione um novo case para o cliente de LLM que você deseja utilizar
- Faça a configuração necessária para o cliente
- Adicione as dependências necessárias no arquivo `backend/requirements.txt`
- Teste o novo cliente