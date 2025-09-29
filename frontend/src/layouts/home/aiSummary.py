import streamlit as st
from time import sleep
from services.ai import AIService

def AISummaryTab(ai_service: AIService):
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