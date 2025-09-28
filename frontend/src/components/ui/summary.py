import streamlit as st
import pandas as pd
import altair as alt
from services.feedback import FeedbackService
from components.charts import donutChart, stackedBarChart
from components.charts import barChart
from typing import Optional

def summary(service: FeedbackService, title: str, branch_id: Optional[int]):    
    # Pega dados da API

    data = service.get_summary(branch_id)

    # Container com métricas
    row = st.container(horizontal=True)

    with row:
        st.metric("Total", data['total'], border=True)
        st.metric("Score", f'{data["score"]:.2f}%', border=True)
        
    
    # row = st.container(horizontal=True)
    # with row:
    #     st.metric("Detratores", data['negative'], border=True)
    #     st.metric("Neutros", data['neutral'], border=True)
    #     st.metric("Promotores", data['positive'], border=True)

    # ------------------------------
    # Criar DataFrame e bandas
    # ------------------------------
    if "details" in data and len(data["details"]) > 0:
        # Extrair scores
        df = pd.DataFrame(data["details"])
        df = df[["origin", "total", "negative", "neutral", "positive"]]

        
        #-------------------------------------------------------------------------------
        # Distribuição de notas
        #-------------------------------------------------------------------------------
        st.subheader("📊 Distribuição de Notas")
        # st.dataframe(df)
        
        container = st.container(horizontal=True)
        with container:
            donutChart(data, f'donut_chart_{title}')
            stackedBarChart(data, f'stacked_bar_chart_{title}')
            
        #-------------------------------------------------------------------------------
        # Dados sobre canais
        #-------------------------------------------------------------------------------
        st.subheader("📊 Distribuição de avaliações por canal")
        
        container = st.container(horizontal=True)
        with container:
            barChart(data, f'bar_chart_{title}')
            
        
        

    else:
        st.write("Nenhum score disponível para gerar gráfico.")
