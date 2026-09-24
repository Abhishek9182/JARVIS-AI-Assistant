import streamlit as st
import psutil


st.set_page_config(
    page_title="JARVIS HUD",
    layout="wide"
)


st.markdown(
    """
    <style>

    .main {
        background-color: #050505;
        color: #00ffff;
    }

    h1, h2, h3 {
        color: #00ffff;
        text-shadow:
            0 0 10px #00ffff;
    }

    .stButton > button {

        background-color: #00ffff;
        color: black;

        font-weight: bold;

        border: 2px solid #00ffff;
        border-radius: 10px;

        box-shadow:
            0 0 15px #00ffff;
    }

    </style>
    """,
    unsafe_allow_html=True
)


st.title("J.A.R.V.I.S COMMAND CENTER")

st.markdown("---")


cpu = psutil.cpu_percent(
    interval=1
)

ram = psutil.virtual_memory()


col1, col2 = st.columns(2)


with col1:

    st.metric(
        "CPU Usage",
        f"{cpu}%"
    )


with col2:

    st.metric(
        "RAM Usage",
        f"{ram.percent}%"
    )


st.markdown("---")

st.success(
    "JARVIS SYSTEM ONLINE"
)