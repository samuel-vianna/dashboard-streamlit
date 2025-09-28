import streamlit as st
from services.feedback import FeedbackService
from services.branch import BranchService
from components.ui.summary import summary
from components.ui.filter import filter

# Services
nps_service = FeedbackService('nps')
csat_service = FeedbackService('csat')
branch_service = BranchService()

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
tab1, tab2 = st.tabs(["NPS", "CSAT"])

with tab1:
    summary(nps_service, "NPS")

with tab2:
    summary(csat_service, "CSAT")

