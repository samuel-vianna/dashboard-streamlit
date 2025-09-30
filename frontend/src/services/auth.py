from typing import Optional
import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

API_URL: str = os.getenv("API_URL", "http://localhost:8000")

class AuthService:

    @staticmethod
    def login(username: str, password: str) -> dict:
        # OAuth2 password form
        res = requests.post(f"{API_URL}/auth/login", data={"username": username, "password": password})
        res.raise_for_status()
        data = res.json()
        token = data.get("access_token")
        if token:
            AuthService.set_token(username, token)
        return data

    @staticmethod
    def logout():
        st.session_state.token = None
        st.session_state.user = None
        st.rerun()

    @staticmethod
    def set_token(username: str, token: str):
        try:
            st.session_state.user = username
            st.session_state.token = token
        except Exception:
            raise Exception("Erro ao salvar token")

    @staticmethod
    def get_token() -> Optional[str]:
        return st.session_state.get("token", None)

    @staticmethod
    def protect():
        """Bloqueia a página se não estiver autenticado"""
        if not AuthService.get_token():
            st.warning("⚠️ Você precisa fazer login para acessar esta página.")
            st.switch_page("main.py")
            st.stop()

    @staticmethod
    def get_headers():
        token = AuthService.get_token()
        if token:
            return {"Authorization": f"Bearer {token}"}
        return {}
