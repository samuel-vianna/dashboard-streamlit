import streamlit as st
import pandas as pd
import altair as alt
from services.feedback import FeedbackService
from components.charts import donutChart, stackedBarChart

def summary(service: FeedbackService, title: str):    
    # Pega dados da API

    data = service.get_summary()

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

        
        st.subheader("📊 Distribuição de Notas")
        # st.dataframe(df)
        
        container = st.container(horizontal=True)
        with container:
            donutChart(data, f'donut_chart_{title}')
            stackedBarChart(data, f'stacked_bar_chart_{title}')
        

    else:
        st.write("Nenhum score disponível para gerar gráfico.")
