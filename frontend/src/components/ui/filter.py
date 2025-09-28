import streamlit as st
from services.branch import BranchService

def filter(service: BranchService):
    branch_options = service.get_branches()
    origin_options = service.get_origins()
    period_options = [
        {"value": "day", "label": "Dia"},
        {"value": "week", "label": "Semana"},
        {"value": "month", "label": "Mês"}]

    container = st.container(horizontal=True)

    with container:
        branch = st.selectbox(
            "Filial",
            branch_options,
            index=None,
            placeholder="Selecione uma cidade...",
            format_func=lambda b: b["name"] if b else "",
            key="branch")
        
        origin = st.selectbox(
            "Canal de Atendimento",
            origin_options,
            index=None,
            placeholder="Selecione um tipo de origem...",
            key="origin")
        
        start_date = st.date_input(
            "Data Inicial",
            value=None,
            format="DD/MM/YYYY",
            key="start_date")
        
        end_date = st.date_input(
            "Data Final",
            value=None,
            format="DD/MM/YYYY",
            key="end_date")
        
        
        period = st.selectbox(
            "Tipo de visualização",
            period_options,
            index=0,
            placeholder="Selecione um tipo de visualização...",
            format_func=lambda p: p["label"] if p else "",
            key="period")    
