import streamlit as st

st.set_page_config(
    page_title="Home - Quadratic Sequence Tutor",
    page_icon="Autotutor.png",
    layout="wide"
)

st.markdown("""
# 📐 Quadratic Sequence Tutor

### CAPS Grade 11 Mathematics

---

## Welcome! 👋

This interactive app helps you learn and teach **quadratic sequences** using the proven CAPS curriculum method.

""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("✨ For Students")
    st.write("""
    - **Learn step-by-step** how to find the general term
    - See **detailed explanations** alongside calculations
    - Practice with **built-in examples**
    - Try **interactive quizzes** to test your understanding
    """)

with col2:
    st.subheader("👨‍🏫 For Teachers")
    st.write("""
    - Access **teacher notes** with deep pedagogy
    - Use **mark-allocated quizzes** (9.5 total marks)
    - Show working to students with **full transparency**
    - Demonstrate the CAPS method clearly
    """)

st.divider()

st.subheader("🚀 How to Use")

tab1, tab2, tab3 = st.tabs(["Quick Start", "Features", "About"])

with tab1:
    st.write("""
    1. Go to the **"Tutor"** page (left sidebar or click below)
    2. Choose your mode: **Student** or **Teacher**
    3. Enter a sequence (e.g., `1, 4, 9, 16`)
    4. Click **Compute general term**
    5. Follow the step-by-step solution!
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
    - Follows Grade 11 curriculum exactly
    - Uses the difference method
    - Teaches system solving
    
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
    
    Created for **Grade 11 Mathematics** education in South Africa (CAPS Curriculum)
    
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

st.caption("📚 Quadratic Sequence Tutor | CAPS Grade 11 | Made with ❤️ for learners and educators")
