import streamlit as st
from services.feedback import FeedbackService
from services.branch import BranchService
from components.ui.summary import summary

# Services
nps_service = FeedbackService('nps')
csat_service = FeedbackService('csat')
branch_service = BranchService()

# Configuração geral
st.set_page_config(page_title="Dashboard Streamlit", layout="wide")

st.title("🚀 Dashboard Streamlit")

branch_options = branch_service.get_branches()

branch = st.selectbox(
    "Filial",
    branch_options,
    index=None,
    placeholder="Selecione uma cidade...",
    format_func=lambda b: b["name"] if b else "")
branch_id = branch["id"] if branch else None


tab1, tab2 = st.tabs(["NPS", "CSAT"])

with tab1:
    summary(nps_service, "NPS", branch_id)

with tab2:
    summary(csat_service, "CSAT", branch_id)

