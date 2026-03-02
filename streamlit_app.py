import streamlit as st

# Configure the main app with rich metadata
st.set_page_config(
    page_title="Maths Tutor | CAPS",
    page_icon="Autotutor.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add Open Graph and social media meta tags via HTML
st.markdown("""
<meta property="og:title" content="Maths Tutor | CAPS" />
<meta property="og:description" content="Interactive math tutor for quadratic sequences. Learn step-by-step with CAPS curriculum methods. Teacher notes, quizzes, and detailed explanations included." />
<meta property="og:type" content="website" />
<meta property="og:url" content="https://autotutor.streamlit.app" />
<meta property="og:image" content="Autotutor.png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Quadratic Sequence Tutor" />
<meta name="twitter:description" content="Learn quadratic sequences with step-by-step CAPS-aligned explanations, teacher notes, and interactive quizzes." />
<meta name="twitter:image" content="Autotutor.png" />

<!-- WhatsApp Specific -->
<meta property="og:site_name" content="Quadratic Sequence Tutor" />
<meta name="apple-mobile-web-app-capable" content="yes" />
""", unsafe_allow_html=True)

# Redirect to home page
st.switch_page("pages/🏠_Home.py")
