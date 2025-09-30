import streamlit as st

def AboutSummaryTab():
    # ------------------------------
    st.header("🎯 Objetivo do Projeto")
    st.write(
        """
        O objetivo deste projeto é **analisar a experiência do usuário**
        por meio de métricas de satisfação, permitindo que a equipe tome
        decisões baseadas em dados para melhorar continuamente os serviços.
        
        Além dos gráficos e relatórios, o dashboard também apresenta um relatório
        de resumo dos dados, gerado dinamicamente com inteligência artificial.
        
        Além disso, o dashboard também apresenta um resumo dos comentários e a classificação
        dos comentários com base em sentimentos, utilizando inteligência artificial.
        """
    )

    # ------------------------------
    st.header("📊 Score NPS e CSAT")
    st.write(
        """
        - **NPS (Net Promoter Score):** mede a probabilidade de recomendação
        do serviço/produto por parte dos usuários.  
        Quanto maior o score, mais leais e satisfeitos os clientes estão.

        - **CSAT (Customer Satisfaction):** avalia o nível de satisfação
        imediata em relação a uma experiência específica.
        """
    )