import streamlit as st
import pandas as pd
import altair as alt
from pages import dashboard, ai_generator, about
from components.sidebar import render_sidebar
from services.nps import NPSService

# Services
nps_service = NPSService()

# Configuração geral
st.set_page_config(page_title="Dashboard Streamlit", layout="wide")

st.title("🚀 Dashboard Streamlit")

# Pega dados da API
nps_data = nps_service.get_all()

# Exibe total encontrado
st.write(f"dados encontrados {nps_data['total']}")

# Container com métricas
row = st.container()

with row:
    col1, col2 = st.columns(2)
    col1.metric("NPS", nps_data['total'], border=True)
    col2.metric("CSAT", 5, border=True)

# ------------------------------
# Criar DataFrame e bandas
# ------------------------------
if "items" in nps_data and len(nps_data["items"]) > 0:
    # Extrair scores
    df = pd.DataFrame(nps_data["items"])
    df = df[["score", "comment", "timestamp"]]

    # Criar bandas de notas
    bins = [0, 6, 8, 10]
    labels = ["Detratores (0-6)", "Neutros (6-8)", "Promotores (8-10)"]
    df["band"] = pd.cut(df["score"], bins=bins, labels=labels, include_lowest=True)

    st.subheader("📊 Distribuição de Notas")
    st.dataframe(df)

    # Contagem por banda
    band_counts = df["band"].value_counts().sort_index()
    band_df = pd.DataFrame({
        "Banda": band_counts.index.astype(str),
        "Quantidade": band_counts.values
    })

    # Gráfico de barras
    chart = alt.Chart(band_df).mark_bar(color="#4CAF50").encode(
        x=alt.X("Banda", sort=None, title="Faixa de Notas"),
        y=alt.Y("Quantidade", title="Quantidade de Avaliações"),
        tooltip=["Banda", "Quantidade"]
    ).properties(
        title="📊 Distribuição de NPS / CSAT por Banda"
    )

    st.altair_chart(chart, use_container_width=True)

else:
    st.write("Nenhum score disponível para gerar gráfico.")
