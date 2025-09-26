import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from services.feedback import SummaryData

def stackedBarChart(data: SummaryData, key: str = "stacked_bar_chart"):
    # -----------------------------------
    # Barras horizontais empilhadas
    # -----------------------------------
    origins = []
    detratores = []
    neutros = []
    promotores = []

    for d in data["details"]:
        total = d["total"] or 1
        origins.append(d["origin"] if d["origin"] else "Indefinido")
        detratores.append(d["negative"] / total * 100)
        neutros.append(d["neutral"] / total * 100)
        promotores.append(d["positive"] / total * 100)

    fig_bar = go.Figure()

    fig_bar.add_trace(go.Bar(
        y=origins,
        x=detratores,
        name="Detratores",
        orientation="h",
        marker=dict(color="#ff4d4f")
    ))
    fig_bar.add_trace(go.Bar(
        y=origins,
        x=neutros,
        name="Neutros",
        orientation="h",
        marker=dict(color="#faad14")
    ))
    fig_bar.add_trace(go.Bar(
        y=origins,
        x=promotores,
        name="Promotores",
        orientation="h",
        marker=dict(color="#52c41a")
    ))

    fig_bar.update_layout(
        barmode="stack",
        xaxis=dict(title="Porcentagem (%)", range=[0, 100]),
        title="Distribuição por Origem"
    )

    st.plotly_chart(fig_bar, use_container_width=True, key=key)
