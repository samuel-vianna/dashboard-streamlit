import streamlit as st
import plotly.graph_objects as go
from services.feedback import SummaryData

def barChart(data: SummaryData, key: str = "stacked_bar_chart"):
    # -----------------------------------
    # Barras verticais - Totais por origem
    # -----------------------------------
    origins = []
    totals = []

    for d in data["details"]:
        origins.append(d["origin"] if d["origin"] else "Indefinido")
        totals.append(d["total"] or 0)

    # Ordenar do maior para o menor
    combined = sorted(zip(origins, totals), key=lambda x: x[1], reverse=True)
    origins, totals = zip(*combined)

    # Calcular porcentagem
    total_sum = sum(totals) or 1
    percentages = [(t / total_sum) * 100 for t in totals]

    # Texto exibido: total + porcentagem
    labels = [f"{t} ({p:.1f}%)" for t, p in zip(totals, percentages)]

    # Criar gráfico
    fig_bar = go.Figure(
        data=[
            go.Bar(
                x=origins,
                y=totals,
                text=labels,
                textposition="auto",
                marker_color="steelblue",
            )
        ]
    )

    fig_bar.update_layout(
        xaxis=dict(title="Origem"),
        yaxis=dict(title="Total"),
        title="Totais por Origem",
    )

    st.plotly_chart(fig_bar, use_container_width=True, key=key)
