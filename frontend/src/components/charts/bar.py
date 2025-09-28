import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from services.feedback import SummaryData


def barChart(data: SummaryData, key: str = "stacked_bar_chart"):
    # Transformar detalhes em DataFrame
    df = pd.DataFrame(data["details"])

    # Garantir valores
    df["origin"] = df["origin"].fillna("Indefinido")
    df["total"] = df["total"].fillna(0)

    # Agrupar por origem e somar totais
    df_grouped = df.groupby("origin", as_index=False)["total"].sum()

    # Ordenar do maior para o menor
    df_grouped = df_grouped.sort_values(by="total", ascending=False)

    # Calcular porcentagem
    total_sum = df_grouped["total"].sum() or 1
    df_grouped["percentage"] = df_grouped["total"] / total_sum * 100

    # Criar labels
    df_grouped["label"] = df_grouped.apply(lambda row: f"{row.total} ({row.percentage:.1f}%)", axis=1)

    # Criar gráfico
    fig_bar = go.Figure(
        data=[
            go.Bar(
                x=df_grouped["origin"],
                y=df_grouped["total"],
                text=df_grouped["label"],
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
