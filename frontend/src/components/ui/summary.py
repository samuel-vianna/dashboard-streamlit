import streamlit as st
import pandas as pd
import altair as alt
from services.feedback import FeedbackService
from components.charts import donutChart, stackedBarChart
from components.charts import barChart
from typing import Optional

def summary(service: FeedbackService, title: str):    
    
    # ------------------------------
    # Pegar dados da API
    # ------------------------------
    
    # Brandh
    branch = st.session_state.get("branch", None)
    branch_id = branch["id"] if branch else None
    
    # Origin
    origin = st.session_state.get("origin", None)

    # Period
    period = st.session_state.get("period", None)
    period_value = period["value"] if period else None
    
    # start and end dates
    start_date = st.session_state.get("start_date", None)
    end_date = st.session_state.get("end_date", None)
    
    print(start_date)
    print(end_date)

    data = service.get_summary(branch_id, origin, period_value, start_date, end_date)

    # ------------------------------
    # Totais
    # ------------------------------
    row = st.container(horizontal=True)

    with row:
        st.metric("Total", data['total'], border=True)
        st.metric("Score", f'{data["score"]:.2f}%', border=True)
        
    # ------------------------------
    # Criar DataFrame e bandas
    # ------------------------------
    if "details" in data and len(data["details"]) > 0:
        # Extrair scores
        df = pd.DataFrame(data["details"])
        df = df[["origin", "total", "negative", "neutral", "positive"]]

        
        # ------------------------------
        # Distribuição de notas
        # ------------------------------
        st.subheader("📊 Distribuição de Notas")
        # st.dataframe(df)
        
        container = st.container(horizontal=True)
        with container:
            donutChart(data, f'donut_chart_{title}')
            stackedBarChart(data, f'stacked_bar_chart_{title}')
            
        # ------------------------------
        # Dados sobre canais
        # ------------------------------
        st.subheader("📊 Distribuição de avaliações por canal")
        
        container = st.container(horizontal=True)
        with container:
            barChart(data, f'bar_chart_{title}')
            
        
        

    else:
        st.write("Sem dados disponíveis para os filtros selecionados.")
