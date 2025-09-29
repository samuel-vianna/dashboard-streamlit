import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from typing import Optional


def barChart(
    data: Optional[pd.DataFrame] = None,
    key: str = "stacked_bar_chart",
    title: str = "Totais por Origem",
    x_col: str = "origin",
    y_col: str = "total",
    label_col: Optional[str] = None,
    color: str = "steelblue"
):
    if data is None or data.empty:
        st.write(f"Nenhum dado disponível para o gráfico: {title}")
        return

    df = data.copy()

    # Garantir valores
    df[x_col] = df[x_col].fillna("Indefinido")
    df[y_col] = df[y_col].fillna(0)

    # Agrupar por coluna X e somar Y
    df_grouped = df.groupby(x_col, as_index=False)[y_col].sum()

    # Ordenar do maior para o menor
    df_grouped = df_grouped.sort_values(by=y_col, ascending=False)

    # Calcular porcentagem
    total_sum = df_grouped[y_col].sum() or 1
    df_grouped["percentage"] = df_grouped[y_col] / total_sum * 100

    # Criar labels
    if label_col:
        df_grouped["label"] = df_grouped[label_col]
    else:
        df_grouped["label"] = df_grouped.apply(lambda row: f"{row[y_col]} ({row.percentage:.1f}%)", axis=1)

    # Criar gráfico
    fig_bar = go.Figure(
        data=[
            go.Bar(
                x=df_grouped[x_col],
                y=df_grouped[y_col],
                text=df_grouped["label"],
                textposition="auto",
                marker_color=color,
            )
        ]
    )

    fig_bar.update_layout(
        xaxis=dict(title=x_col.capitalize()),
        yaxis=dict(title=y_col.capitalize()),
        title=title,
    )

    st.plotly_chart(fig_bar, use_container_width=True, key=key)
