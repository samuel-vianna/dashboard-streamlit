import streamlit as st
from datetime import datetime
from services.ai import AIService
from services.branch import BranchService
from components.ui.authRoute import AuthRoute

ai_service = AIService()
branch_service = BranchService()

AuthRoute()

st.title("🤖 Gerar Feedback com IA")

st.write("Utilize essa página para gerar novos dados de feedback com inteligência artificial. Você pode escolher o tipo de feedback e a quantidade de feedbacks a serem gerados.")

# Inputs
feedback_type = st.selectbox("Tipo de feedback", ["nps", "csat"], index=0, format_func=lambda x: x.upper())
amount = st.number_input("Quantidade de feedbacks", min_value=1, max_value=100, value=10)

with st.spinner('Buscando filiais...'):
    branch_options = branch_service.get_branches()
    branch = st.selectbox(
        "Filial",
        branch_options,
        index=0,
        placeholder="Selecione uma filial...",
        format_func=lambda b: b["name"] if b else ""
        )

c2 = st.container(horizontal=True)
with c2:
    date = st.date_input("Data", datetime.today())
    max_time_diff = st.number_input("Máxima diferença de tempo (horas)", min_value=0, max_value=24, value=1)

context = st.text_area("Contexto (opcional)")

# Botão para enviar
if st.button("Gerar Feedback"):
    with st.spinner("Processando..."):
        try:
            branch_id = branch["id"] if branch else None
            payload = {
                "type": feedback_type,
                "amount": amount,
                "context": context,
                "date": datetime.combine(date, datetime.now().time()).isoformat(),
                "max_time_diff": max_time_diff,
                "branch_id": branch_id
            }
            res = ai_service.generate_feedback(payload)

            if res.status_code == 200:
                st.success("Feedback gerado com sucesso!")
                st.json(res.json())
            else:
                st.error(f"Erro: {res.status_code} — {res.text}")

        except Exception as e:
            st.error(f"Erro ao gerar feedback: {e}")
