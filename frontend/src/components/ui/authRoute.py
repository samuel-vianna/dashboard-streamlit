from services.auth import AuthService
import streamlit as st

def AuthRoute():    
    # Proteger página
    AuthService.protect()

    st.sidebar.success(f"👤 Logado como {st.session_state.user}")
    if st.sidebar.button("🚪 Logout"):
        AuthService.logout()