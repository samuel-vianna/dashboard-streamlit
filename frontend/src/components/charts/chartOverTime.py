import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from typing import Any


def chartOverTime(data: Any):
    # Transformar detalhes em DataFrame
    df = pd.DataFrame(data["details"])

    # Garantir que period é datetime
    df["period"] = pd.to_datetime(df["period"])

    # Agrupar por período (somando todas as origens)
    df_grouped = df.groupby("period").agg({
        "negative": "sum",
        "neutral": "sum",
        "positive": "sum"
    }).reset_index()

    # Ordenar por período
    df_grouped = df_grouped.sort_values("period")

    # Criar gráfico de barras empilhadas
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df_grouped["period"],
        y=df_grouped["negative"],
        name="Detratores",
        marker_color="#ff4d4f"  # vermelho
    ))

    fig.add_trace(go.Bar(
        x=df_grouped["period"],
        y=df_grouped["neutral"],
        name="Neutros",
        marker_color="#faad14"  # amarelo
    ))

    fig.add_trace(go.Bar(
        x=df_grouped["period"],
        y=df_grouped["positive"],
        name="Promotores",
        marker_color="#52c41a"  # verde
    ))

    fig.update_layout(
        barmode="stack",
        title="Distribuição de Feedback ao longo do tempo",
        xaxis_title="Período",
        yaxis_title="Quantidade",
        legend_title="Categoria",
    )

    st.plotly_chart(fig, use_container_width=True)
