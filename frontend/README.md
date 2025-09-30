# Frontend (Streamlit)

Este é o serviço **frontend** desenvolvido em **Streamlit** para o Dashboard de Feedback — NPS & CSAT.
Ele fornece a interface interativa para visualização de métricas, relatórios e análises geradas pelo backend.

---

## 📦 Requisitos

* **Python 3.11+**
* Biblioteca Streamlit

Arquivos principais:

* [`requirements.txt`](./requirements.txt)
* Código principal: [`src/main.py`](./src/main.py)

---

## ▶️ Rodando o frontend

### 1. Configurar variáveis de ambiente

O frontend também pode utilizar variáveis de ambiente para configuração.
Na raiz do frontend existe um arquivo `.env.example`.
Você deve copiá-lo para `.env` e ajustar os valores conforme sua necessidade:

```bash
cp .env.example .env
```

---

### 2. Criar e ativar ambiente virtual

```bash
python -m venv venv_frontend
source venv_frontend/bin/activate
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4. Rodar o frontend localmente

```bash
streamlit run src/main.py
```

Após rodar o comando, acesse o frontend em:

```
http://localhost:8500
```

---

## 📂 Estrutura de Pastas

```bash
.
├── README.md
├── requirements.txt
├── src
│   ├── components      # Componentes visuais reutilizáveis
│   ├── layouts         # Layouts da aplicação
│   ├── main.py         # Ponto de entrada da aplicação Streamlit
│   ├── pages           # Páginas específicas do dashboard
│   └── services        # Serviços e integrações com backend
└── venv_frontend       # Ambiente virtual
```

---

## 🔗 Integração com Backend

O frontend se comunica com o backend via APIs REST expostas pelo FastAPI.
Certifique-se de que o backend esteja rodando antes de iniciar o frontend.
Por padrão, o frontend buscará a API no endereço configurado no `.env`.
