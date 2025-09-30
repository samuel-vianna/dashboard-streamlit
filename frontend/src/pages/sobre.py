
import streamlit as st
from components.ui.authRoute import AuthRoute

AuthRoute()

st.title("ℹ Sobre este projeto")
st.write("""
Este projeto foi desenvolvido para mostrar um exemplo de integração entre
FastAPI e Streamlit.

Funcionalidades:
- Dashboard principal
- Geração de dados usando IA
- Documentação do projeto
""")
