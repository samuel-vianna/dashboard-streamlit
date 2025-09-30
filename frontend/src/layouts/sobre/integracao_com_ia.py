import streamlit as st

def AboutIntegrationTab():
    # ------------------------------
    st.header("🗄️ Como é gerada a massa de dados")
    st.write(
        """
        Os dados utilizados neste dashboard são **gerados com inteligência artificial**
        para fins de teste e desenvolvimento.  
        Cada entrada contém informações de feedback de usuários fictícios,
        incluindo notas e comentários, que são processados para gerar gráficos
        e relatórios.
        """
    )

    st.subheader("Dados gerados com IA")

    st.write(
        """
        Para cada feedback o modelo gera os seguintes dados:
        - Nota de acordo com o tipo de feedback:
            - NPS: notas de 0 a 10.
            - CSAT: notas de 1 a 5.
        - Comentário coerente com a nota
        - Data de envio
        - Origem do atendimento:
            - Site
            - App
            - Telefone
            - Email
            - Chat
            - Presencial
        """
    )