import streamlit as st
from services.feedback import FeedbackService
from services.branch import BranchService
from services.ai import AIService
from components.ui.summary import summary
from components.ui.filter import filter
from layouts.home.aiSummary import AISummaryTab
from layouts.home.sentiments import SentimentsTab

# Services
nps_service = FeedbackService('nps')
csat_service = FeedbackService('csat')
branch_service = BranchService()
ai_service = AIService()


# Configuração geral
st.set_page_config(page_title="Dashboard Streamlit", layout="wide")

st.title("🚀 Dashboard Streamlit")

# ------------------------------
# Filtros
# ------------------------------
filter(branch_service)

# ------------------------------
# Tabs
# ------------------------------
tab1, tab2, tab3, tab4 = st.tabs(["NPS", "CSAT", "Análise de comentários", "Resumo com IA",])

with tab1:
    summary(nps_service, "NPS")

with tab2:
    summary(csat_service, "CSAT")

with tab3:
    SentimentsTab(nps_service, csat_service)

with tab4:    
    AISummaryTab(ai_service)
