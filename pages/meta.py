"""
Meta endpoint for social media previews
Helps with OpenGraph when sharing Streamlit links
"""
import streamlit as st

st.set_page_config(page_title="Math Tutor", page_icon="Autotutor.png")

st.markdown("""
# Share this app!

## Social Media Preview

When you share this link on social media, it shows:
- **Title:** Math Tutor | CAPS
- **Description:** Interactive math tutor for learning Math
- **Icon:** "Autotutor.png"

## Copy your share link:
""")


st.code("https://autotutor.streamlit.app", language="text")

st.info("Tip: Paste this URL on WhatsApp, Facebook, or Twitter for a rich preview!")
