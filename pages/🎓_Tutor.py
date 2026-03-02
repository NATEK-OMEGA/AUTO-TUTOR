import streamlit as st
from seq_math_app import main as run_app

# Configure page metadata for social sharing and browser display
st.set_page_config(
    page_title="AUTO-Tutor | CAPS Mathematics",
    page_icon="Autotutor.png",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "AUTO-Tutor – an interactive South African CAPS mathematics learning tool for Grades 10–12."
    }
)

# simply delegate to the main application logic

run_app()

# note: original tutor implementation has been migrated to seq_math_app.py
