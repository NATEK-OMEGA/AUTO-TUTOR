import streamlit as st

st.set_page_config(
    page_title="Home - AUTO-Tutor",
    page_icon="Autotutor.png",
    layout="wide"
)

st.markdown("""
# 📐 AUTO-Tutor

### CAPS Grade 10–12 Mathematics

---

## Welcome! 👋

This interactive app helps you learn and teach **many topics from the CAPS mathematics curriculum** using interactive tools and step-by-step reasoning.

""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("✨ For Students")
    st.write("""
    - **Learn step-by-step** with CAPS‑aligned explanations across grades 10–12
    - Practice using interactive calculators and visualisations
    - Work through example problems and self‑assess with quizzes
    """)

with col2:
    st.subheader("👨‍🏫 For Teachers")
    st.write("""
    - Access **teacher notes** and curriculum references across all topics
    - Use **mark-allocated quizzes** for formative assessment
    - Show full working with clear mathematical language
    - Support learners from Grade 10 through 12
    """)

st.divider()

st.subheader("🚀 How to Use")

tab1, tab2, tab3 = st.tabs(["Quick Start", "Features", "About"])

with tab1:
    st.write("""
    1. Go to the **"Tutor"** page (use the sidebar or the buttons below)
    2. Choose your mode: **Student** or **Teacher**
    3. Select a grade and a topic from the dropdowns
    4. Enter the requested values or expressions
    5. Follow the step-by-step explanations and try the quizzes!
    """)
    st.info("💡 **Tip:** Try the examples first to see how it works!")

with tab2:
    st.write("""
    ### What's Included
    
    ✅ **Mathematical Accuracy**
    - Clean polynomial formatting (no `1n²`, no `+0` terms)
    - Full working shown in calculation steps
    - Verification of answers
    
    ✅ **CAPS Alignment**
    - Covers topics from Grades 10–12
    - Explanations and examples correspond to CAPS outcomes
    - Builds algebraic and geometric reasoning
    
    ✅ **Interactive Learning**
    - Student and Teacher modes
    - Built-in examples
    - Quiz system with marks
    - Teacher notes for pedagogy
    
    ✅ **Accessibility**
    - Works on any device
    - No installation needed
    - Free and open
    """)

with tab3:
    st.write("""
    ### About This App
    
    Created as an educational tool for South African CAPS Mathematics (Grades 10–12)
    
    **Features:**
    - Streamlit-based web app
    - Python backend
    - Mobile-friendly interface
    - Easy to share
    
    **Use Cases:**
    - Classroom demonstrations
    - Self-study for learners
    - Teacher preparation
    - Homework help
    
    **Built with:**
    - Streamlit
    - Python
    - Love for education 💚
    """)

st.divider()

st.markdown("""
---

### 🎯 Start Learning Now!

Click the **"Tutor"** link in the sidebar to begin, or select a mode:
""")

col1, col2 = st.columns(2)

with col1:
    if st.button("👨‍🎓 Student Mode", use_container_width=True):
        st.switch_page("pages/🎓_Tutor.py")

with col2:
    if st.button("👨‍🏫 Teacher Mode", use_container_width=True):
        st.switch_page("pages/🎓_Tutor.py")

st.divider()

st.caption("📚 AUTO-Tutor | CAPS Mathematics Grades 10–12 | Made with ❤️ for learners and educators")
