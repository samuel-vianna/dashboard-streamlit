import streamlit as st
import pandas as pd
from services.feedback import FeedbackService
from components.charts import barChart

def SentimentsTab(nps_service: FeedbackService, csat_service: FeedbackService):
    st.subheader("Análise de sentimentos com IA")
    
    with st.spinner("Obtendo lista de comentários..."):
        nps_sentiments_data = nps_service.get_sentiments()
        csat_sentiments_data = csat_service.get_sentiments()
                
    st.write(f"Os comentários de NPS e CSAT foram categorizados em sentimentos com inteligência artificial.")
        
    nps_df_sentiments = pd.DataFrame(list(nps_sentiments_data.items()), columns=["Sentimento", "Quantidade"])
    barChart(
        data=nps_df_sentiments,
        title="Distribuição de Sentimentos (NPS)",
        x_col="Sentimento",
        y_col="Quantidade",
        color="steelblue",
        key="nps_sentiment_bar_chart"
    )
    
    csat_df_sentiments = pd.DataFrame(list(csat_sentiments_data.items()), columns=["Sentimento", "Quantidade"])
    barChart(
        data=csat_df_sentiments,
        title="Distribuição de Sentimentos (CSAT)",
        x_col="Sentimento",
        y_col="Quantidade",
        color="steelblue",
        key="csat_sentiment_bar_chart"
    )
    