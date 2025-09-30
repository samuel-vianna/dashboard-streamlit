import streamlit as st
import streamlit_mermaid as stmd


def AboutArchitectureTab():
    # ------------------------------
    st.header("👨‍💻 Arquitetura do Projeto")

    st.write(
        """
        Este projeto foi desenvolvido **100% em Python**, combinando as seguintes tecnologias:

        - **Frontend:** [Streamlit](https://streamlit.io/) para interface interativa e visualização de dados.  
        - **Backend:** [FastAPI](https://fastapi.tiangolo.com/) para criação de APIs rápidas e escaláveis.  
        - **Banco de dados:** [PostgreSQL](https://www.postgresql.org/) para persistência dos dados.  
        """
    )

    # ------------------------------
    st.subheader("📦 Estrutura do Banco de Dados (exemplo simplificado)")

    
    database_diagram = """
   erDiagram
    USER {
        int id PK
        varchar username
        varchar password
    }

    BRANCH {
        int id PK
        varchar name
    }

    NPSFEEDBACK {
        int id PK
        int score
        text comment
        timestamp timestamp
        varchar origin
        int branch_id FK
        varchar sentiment
    }

    CSATFEEDBACK {
        int id PK
        int score
        text comment
        timestamp timestamp
        varchar origin
        int branch_id FK
        varchar sentiment
    }

    BRANCH ||--o{ NPSFEEDBACK : "possui"
    BRANCH ||--o{ CSATFEEDBACK : "possui"

    """

    stmd.st_mermaid(database_diagram)
    st.caption("O diagrama acima mostra um resumo da estrutura do banco de dados.")

    st.write(
        """
        A divisão de comentários em 2 bancos (NPS e CSAT) foi feita considerando os seguintes aspectos:
        - **Facilidade de busca**: consultas diretas ficam mais claras e rápidas (ex.: buscar só NPS ou só CSAT).
        - **Extensão futura**: caso seja necessário adicionar atributos específicos de NPS ou CSAT (ex.: categorias, tags, diferentes métodos de coleta)
        - **Escalabilidade**: cada métrica pode evoluir de forma independente conforme o projeto cresce.
        """
    )

    # ------------------------------
    st.subheader("🏗️ Arquitetura Geral")

    st.write(
        """
        O projeto segue uma arquitetura modular, separando frontend, backend e banco de dados.  
        Abaixo, um diagrama simplificado:
        """
    )
    
    mermaid_code = """
    graph TD
        A[Streamlit Frontend] -->|chama APIs| B(FastAPI Backend)
        B --> C[(PostgreSQL Database)]
        B --> D[LangChain + Modelos de IA]
        D --> E[Gemini API]
        D --> F[Suporte futuro para outros LLMs]
    """

    stmd.st_mermaid(mermaid_code)

    st.caption("O diagrama acima mostra como os componentes se conectam entre si.")

    # ------------------------------
    st.subheader("🧪 Testes")

    st.write(
        """
        Os testes unitários no backend são escritos com **[pytest](https://docs.pytest.org/)**,
        garantindo qualidade e confiabilidade na lógica de negócio e APIs.
        """
    )

    # ------------------------------
    st.subheader("🤖 Inteligência Artificial")

    st.write(
        """
        Este projeto utiliza a biblioteca **LangChain** para integrar IA ao backend.  
        - Atualmente, há suporte para o **Google Gemini**.  
        - A arquitetura foi pensada para facilitar a adição de **novos modelos** no futuro.  
        
        No **README** você encontra instruções de como configurar e adicionar outros LLMs.
        """
    )

    # ------------------------------
    st.subheader("📂 Estrutura do Projeto")

    st.write(
        """
        A organização das pastas do **frontend** e do **backend** é detalhada no README.  
        Lá você encontra informações de como rodar e buildar o projeto.
        """
    )

    st.markdown(
        """
        👉 [Veja o README no GitHub](https://github.com/samuel-vianna/dashboard-streamlit)
        """
    )
