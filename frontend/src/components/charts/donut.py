import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from services.feedback import SummaryData

def donutChart(data: SummaryData, key: str = "donut_chart"):

    # ---------------------------
    # Donut Chart (geral)
    # ---------------------------
    sizes = [data["negative"], data["neutral"], data["positive"]]
    labels = ["Detratores", "Neutros", "Promotores"]
    colors = ["#ff4d4f", "#faad14", "#52c41a"]

    fig_donut = px.pie(
        values=sizes,
        names=labels,
        color=labels,
        color_discrete_map={
            "Detratores": "#ff4d4f",
            "Neutros": "#faad14",
            "Promotores": "#52c41a"
        },
        hole=0.5
    )
    fig_donut.update_traces(textinfo="percent+label")

    st.plotly_chart(fig_donut, use_container_width=True, key=key)