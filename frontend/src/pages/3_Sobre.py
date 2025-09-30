
import streamlit as st
from components.ui.authRoute import AuthRoute
from layouts.sobre import AboutSummaryTab, AboutArchitectureTab, AboutIntegrationTab, AboutGenerateDataTab

AuthRoute()

st.set_page_config(page_title="Sobre o Projeto")

st.title("ℹ️ Sobre o Projeto")

st.write(
    """
    Bem-vindo à página de **informações do projeto**.  
    Aqui você encontra detalhes sobre os objetivos, as métricas usadas
    e como interagir com o dashboard.
    """
)

tab1, tab2, tab3, tab4 = st.tabs(["Resumo", 'Arquitetura do projeto', "Integração com IA", "Gerando dados pelo dashboard"])


with tab1:
    AboutSummaryTab()
    
with tab2:
    AboutArchitectureTab()
    
with tab3:
    AboutIntegrationTab()
    
with tab4:
    AboutGenerateDataTab()



