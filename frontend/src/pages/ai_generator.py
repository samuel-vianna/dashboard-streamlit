
import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("🤖 Gerar Dados com IA")
prompt = st.text_area("Digite o prompt para gerar dados")
if st.button("Gerar"):
    with st.spinner("Processando..."):
        try:
            res = requests.post(f"{API_URL}/ai/generate", json={"input": prompt})
            st.success("Dados gerados com sucesso!")
            st.json(res.json())
        except Exception as e:
            st.error(f"Erro: {e}")
