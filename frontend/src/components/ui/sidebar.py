import streamlit as st

def render_sidebar():
    st.sidebar.title("Menu")
    return st.sidebar.radio("Navegação", ["Dashboard", "Gerar Dados IA", "Sobre"])
