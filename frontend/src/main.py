import streamlit as st
from services.feedback import FeedbackService
from components.ui.summary import summary

# Services
nps_service = FeedbackService('nps')
csat_service = FeedbackService('csat')

# Configuração geral
st.set_page_config(page_title="Dashboard Streamlit", layout="wide")

st.title("🚀 Dashboard Streamlit")

branch = st.selectbox(
    "Filial",
    ("SP", "BH"),
    index=None,
    placeholder="Selecione uma cidade...",
)


tab1, tab2 = st.tabs(["NPS", "CSAT"])

with tab1:
    summary(nps_service, "NPS")

with tab2:
    summary(csat_service, "CSAT")

