import streamlit as st
from services.branch import BranchService

def filter(service: BranchService):
    branch_options = service.get_branches()
    origin_options = service.get_origins()

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

