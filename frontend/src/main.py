import streamlit as st
from services.feedback import FeedbackService
from services.branch import BranchService
from services.ai import AIService
from components.ui.summary import summary
from components.ui.filter import filter
from time import sleep

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
tab1, tab2, tab3 = st.tabs(["NPS", "CSAT", "Resumo com IA"])

with tab1:
    summary(nps_service, "NPS")

with tab2:
    summary(csat_service, "CSAT")

# ------------------------------
# Resumo com IA
# ------------------------------
with tab3:    
    st.subheader("🤖 Resumo com IA")
    
    st.write(f"Resumo gerado com inteligência artificial a partir dos dados obtidos.")
    
    # Feedback gerado com IA
    with st.spinner("Gerando feedback com inteligência artificial…"):
        nps_data = st.session_state.get("nps_data", None)
        csat_data = st.session_state.get("csat_data", None)
        feedback = ai_service.generate_feedback(nps_data, csat_data)
        
    try:
        feedbackMessage = feedback.get("summary") if feedback else "Sem feedback gerado."
    except Exception:
        feedbackMessage = "Erro ao gerar feedback."
    
    def stream_data():
        for word in feedbackMessage.split(" "):
            yield word + " "
            sleep(0.02)


        for word in feedbackMessage.split(" "):
            yield word + " "
    
    st.write_stream(stream_data)
