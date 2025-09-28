import streamlit as st
import plotly.graph_objects as go
from services.feedback import SummaryData


def stackedBarChart(data: SummaryData, key: str = "stacked_bar_chart"):
    # -----------------------------------
    # Barras horizontais empilhadas
    # -----------------------------------
    rows = []

    for d in data["details"]:
        total = d["total"] or 1
        origin = d["origin"] if d["origin"] else "Indefinido"
        rows.append({
            "origin": origin,
            "detratores": round(d["negative"] / total * 100, 2),
            "neutros": round(d["neutral"] / total * 100, 2),
            "promotores": round(d["positive"] / total * 100, 2),
        })

    # Ordena pela origem (alfabética)
    rows.sort(key=lambda r: r["origin"], reverse=True)

    origins = [r["origin"] for r in rows]
    detratores = [r["detratores"] for r in rows]
    neutros = [r["neutros"] for r in rows]
    promotores = [r["promotores"] for r in rows]

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
