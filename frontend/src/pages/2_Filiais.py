import streamlit as st
from datetime import datetime
from services.branch import BranchService
from components.ui.authRoute import AuthRoute

branch_service = BranchService()

AuthRoute()

st.title("🏬 Cadastrar Filial")

st.write("Utilize essa página cadastrar novas filiais para o dashboard.")

# Inputs
name = st.text_input("Nome", placeholder="Nome da filial")

# Botão para enviar
if st.button("Cadastrar Filial"):
    with st.spinner("Processando..."):
        try:
            res = branch_service.create_branch(name)

            if res.status_code == 200:
                st.success("Filial cadastrada com sucesso!")
                st.json(res.json())
            else:
                st.error(f"Erro: {res.status_code} — {res.text}")

        except Exception as e:
            st.error(f"Erro ao cadastrar filial: {e}")
