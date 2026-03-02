import streamlit as st
import math
from typing import List
import matplotlib.pyplot as plt
import numpy as np
from topics.grade10 import teach_trigonometry, teach_probability_statistics

# ------------------------------------------
# Grade 11 topic handlers with step-by-step pedagogy
# ------------------------------------------

def teach_linear_functions(show_teacher_notes: bool, show_quizzes: bool) -> None:
    st.subheader("Linear Functions & Graphs (Grade 11)")
    st.write("Explore linear equations y = mx + c and graph their properties.")
    
    col1, col2 = st.columns(2)
    with col1:
        m = st.number_input("Slope m", value=2.0, format="%.2f")
    with col2:
        c = st.number_input("y-intercept c", value=1.0, format="%.2f")
    
    if st.button("Analyse linear function"):
        # STEP 0: Display function
        col_l, col_r = st.columns([2, 3])
        with col_l:
            st.latex(rf"y = {m}x + {c}")
        with col_r:
            st.write("**STEP 0** – The linear function in gradient-intercept form.")
        
        if show_teacher_notes:
            with st.expander("📚 Teacher Notes (Gradient-Intercept Form)"):
                st.write("**y = mx + c** where m = gradient (slope), c = y-intercept. This is the standard form in CAPS.")
        
        # STEP 1: Identify gradient and intercept
        col_l, col_r = st.columns([2, 3])
        with col_l:
            st.latex(rf"\text{{Gradient}}: m = {m}")
            st.latex(rf"\text{{y-intercept}}: c = {c}")
        with col_r:
            st.write("**STEP 1** – Extract gradient and intercept from equation.")
        
        # STEP 2: Calculate some points
        col_l, col_r = st.columns([2, 3])
        with col_l:
            x_vals = [0, 1, 2, -1]
            y_vals = [m*x + c for x in x_vals]
            points_str = ", ".join([f"({x}, {y})" for x, y in zip(x_vals, y_vals)])
            st.latex(rf"\text{{Points on line:}}\ " + points_str[:50])
        with col_r:
            st.write("**STEP 2** – Substitute x-values to find y-coordinates.")
            for x, y in zip(x_vals[:2], y_vals[:2]):
                st.write(f"  When x={x}: y = {m}({x}) + {c} = {y}")
        
        # STEP 3: Interpret slope
        col_l, col_r = st.columns([2, 3])
        with col_l:
            if m > 0:
                st.success(f"✓ Gradient m = {m} > 0: Line slopes **UPWARD** (positive increase)")
            elif m < 0:
                st.warning(f"⚠ Gradient m = {m} < 0: Line slopes **DOWNWARD** (negative decrease)")
            else:
                st.info(f"= Gradient m = {m}: Line is **HORIZONTAL**")
        with col_r:
            st.write("**STEP 3** – Interpret the slope to understand line direction.")
        
        # STEP 4: Plot the function
        fig, ax = plt.subplots(figsize=(8, 6))
        x_range = np.linspace(-5, 5, 100)
        y_range = m * x_range + c
        ax.plot(x_range, y_range, 'b-', linewidth=2, label=f'y = {m}x + {c}')
        ax.plot([x for x in x_vals if -5 <= x <= 5], [y for x, y in zip(x_vals, y_vals) if -5 <= x <= 5], 'ro', markersize=8, label='Points')
        ax.axhline(y=0, color='k', linewidth=0.5)
        ax.axvline(x=0, color='k', linewidth=0.5)
        ax.grid(True, alpha=0.3)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title(f'Graph of y = {m}x + {c}')
        ax.legend()
        ax.set_xlim(-5, 5)
        ax.set_ylim(-10, 10)
        st.pyplot(fig)
        
        if show_teacher_notes:
            with st.expander("📚 Teacher Notes (Graphing)"):
                st.write(
                    "Always identify two key points: (0, c) on the y-axis and find another using the slope. "
                    "Use rise/run to understand gradient: for every 1 unit right, go m units up/down."
                )
    
    if st.button("Find x-intercept"):
        # Find where y = 0
        x_intercept = -c / m if m != 0 else None
        col_l, col_r = st.columns([2, 3])
        with col_l:
            st.latex(rf"0 = {m}x + {c}")
            st.latex(rf"{m}x = {-c}")
            if x_intercept is not None:
                st.latex(rf"x = \frac{{{-c}}}{{{m}}} = {x_intercept:.4f}")
        with col_r:
            st.write("**Finding x-intercept** by setting y=0.")
        
        if x_intercept is not None:
            st.success(f"✓ x-intercept (where line crosses x-axis): **x = {x_intercept:.4f}**")
    
    if show_quizzes:
        with st.expander("📝 Quiz: Linear Functions"):
            st.write("**Question 1 (2 marks):** If y = 2x + 3, find y when x = 5.")
            ans1 = st.text_input("Your answer", key="quiz_lin_1")
            if st.button("Check Q1", key="check_lin_1"):
                if ans1.strip() == "13":
                    st.success("✓ Correct! y = 2(5) + 3 = 10 + 3 = 13. **[2 marks]**")
                else:
                    st.error(f"Expected: 13. Your answer: {ans1}")
            
            st.write("**Question 2 (3 marks):** Find the y-intercept of the line 4x − 2y = 8.")
            ans2 = st.text_input("Your answer (y = ...)", key="quiz_lin_2")
            if st.button("Check Q2", key="check_lin_2"):
                if "-4" in ans2 or "−4" in ans2:
                    st.success("✓ Correct! Rearrange: −2y = −4x + 8 → y = 2x − 4. y-intercept = −4. **[3 marks]**")
                else:
                    st.error("Expected: −4. Your answer: " + ans2)



def teach_quadratic_sequences(show_teacher_notes: bool, show_quizzes: bool) -> None:
    # Quadratic sequences - delegate to the comprehensive quadratic module
    from topics import quadratic as quad
    quad.quadratic_sequence_module(show_teacher_notes=show_teacher_notes, show_quizzes=show_quizzes)


def teach_exponential_functions(show_teacher_notes: bool, show_quizzes: bool) -> None:
    st.subheader("Exponential & Logarithmic Functions (Grade 11)")
    st.write("Evaluate exponential expressions y = ab^x and understand exponential growth.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        a = st.number_input("Coefficient a", value=2.0, format="%.2f")
    with col2:
        b = st.number_input("Base b (b > 0)", value=2.0, format="%.2f")
    with col3:
        x_end = st.number_input("Max x to plot", value=4.0, format="%.1f")
    
    if st.button("Calculate exponential"):
        # STEP 0: Display formula
        col_l, col_r = st.columns([2, 3])
        with col_l:
            st.latex(r"\textbf{Formula:}\ y = ab^x")
        with col_r:
            st.write("**STEP 0** – Exponential function form (a = amplitude, b = base).")
        
        # STEP 1: Calculate some points
        col_l, col_r = st.columns([2, 3])
        with col_l:
            x_vals = [0, 1, 2, 3]
            y_vals = [a * (b ** x) for x in x_vals]
            for x, y in zip(x_vals[:4], y_vals[:4]):
                st.latex(rf"x={x}:\ y = {a} \cdot {b}^{{{x}}} = {y:.4f}")
        with col_r:
            st.write("**STEP 1** – Substitute x-values and calculate y.")
        
        if show_teacher_notes:
            with st.expander("📚 Teacher Notes (STEP 1)"):
                st.write(
                    "Notice the y-values! If b > 1, the values grow rapidly. If 0 < b < 1, they decay. "
                    "This is **exponential** growth or decay."
                )
        
        # STEP 2: Compare with linear growth
        col_l, col_r = st.columns([2, 3])
        with col_l:
            st.markdown("**Exponential vs Linear:**")
            linear_y = [a + 0.5*x for x in x_vals]
            comparison = "x | y (exp) | y (lin)\\n" + "---" * 3 + "\n"
            for x, y_exp, y_lin in zip(x_vals, y_vals, linear_y):
                comparison += f"{int(x)} | {y_exp:.2f} | {y_lin:.2f}\\n"
            st.write(comparison)
        with col_r:
            st.write("**STEP 2** – Exponential grows (or decays) much faster than linear!")
        
        if show_teacher_notes:
            with st.expander("📚 Teacher Notes (Growth Rate)"):
                st.write(
                    "Exponential functions dominate linear functions over time. "
                    "This is why compound interest and bacterial growth are exponential."
                )
        
        # STEP 3: Plot
        fig, ax = plt.subplots(figsize=(8, 6))
        x_range = np.linspace(0, x_end, 100)
        y_range = a * (b ** x_range)
        ax.plot(x_range, y_range, 'b-', linewidth=2, label=f'y = {a} · {b}^x (exponential)')
        ax.plot(x_vals, y_vals, 'bo', markersize=8)
        ax.grid(True, alpha=0.3)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title(f'Exponential Function: y = {a} · {b}^x')
        ax.legend()
        st.pyplot(fig)
        
        if show_teacher_notes:
            with st.expander("📚 Teacher Notes (Graph Shape)"):
                st.write(
                    f"Base b = {b}. If b > 1, curve curves upward (growth). "
                    f"If 0 < b < 1, curve approaches horizontal axis (decay)."
                )
    
    if show_quizzes:
        with st.expander("📝 Quiz: Exponential Functions"):
            st.write("**Question 1 (2 marks):** If y = 2 · 3^x, find y when x = 2.")
            ans1 = st.text_input("Your answer", key="quiz_exp_1")
            if st.button("Check Q1", key="check_exp_1"):
                if ans1.strip() == "18":
                    st.success("✓ Correct! y = 2 · 3² = 2 · 9 = 18. **[2 marks]**")
                else:
                    st.error(f"Expected: 18. Your answer: {ans1}")
            
            st.write("**Question 2 (2 marks):** Is exponential growth faster than linear growth over time?")
            ans2 = st.text_input("Yes/No", key="quiz_exp_2")
            if st.button("Check Q2", key="check_exp_2"):
                if ans2.lower().strip() in ["yes", "y"]:
                    st.success("✓ Correct! Exponential dominates linear in the long run. **[2 marks]**")
                else:
                    st.error("Expected: Yes")


def teach_euclidean_geometry(show_teacher_notes: bool, show_quizzes: bool) -> None:
    st.subheader("Euclidean Geometry (Grade 11)")
    st.write("Explore angle properties, parallel lines, and circle theorems.")
    
    angle_type = st.radio("Select angle property to explore", 
                          ["Supplementary Angles", "Alternate Angles", "Corresponding Angles", "Angle at Centre"])
    
    if angle_type == "Supplementary Angles":
        angle = st.slider("Choose angle (°)", 0, 180, 45)
        if st.button("Show supplementary"):
            col_l, col_r = st.columns([2, 3])
            with col_l:
                st.latex(rf"\text{{Angle 1}} = {angle}°")
                st.latex(rf"\text{{Angle 2}} = 180° - {angle}° = {180-angle}°")
            with col_r:
                st.write("**STEP 0** – Supplementary angles sum to 180° (on a straight line).")
            
            col_l, col_r = st.columns([2, 3])
            with col_l:
                st.latex(rf"{angle}° + {180-angle}° = 180°\ \checkmark")
            with col_r:
                st.write("**STEP 1** – Verify they sum to 180°.")
            
            # Draw angles
            fig, ax = plt.subplots(figsize=(8, 6))
            angle_rad = math.radians(angle)
            # First angle
            x1 = math.cos(angle_rad)
            y1 = math.sin(angle_rad)
            ax.arrow(0, 0, 1, 0, head_width=0.05, head_length=0.05, fc='blue', ec='blue', linewidth=2)
            ax.arrow(0, 0, x1, y1, head_width=0.05, head_length=0.05, fc='red', ec='red', linewidth=2)
            # Angle arc
            arc_angles = np.linspace(0, angle_rad, 50)
            arc_r = 0.2
            ax.plot(arc_r * np.cos(arc_angles), arc_r * np.sin(arc_angles), 'g-', linewidth=2)
            ax.text(0.3, 0.1, f"{angle}°", fontsize=12, color='green')
            
            # Second angle (supplementary)
            ax.arrow(0, 0, -x1, -y1, head_width=0.05, head_length=0.05, fc='orange', ec='orange', linewidth=2)
            arc_angles2 = np.linspace(angle_rad, math.pi, 50)
            ax.plot(arc_r * np.cos(arc_angles2), arc_r * np.sin(arc_angles2), 'm-', linewidth=2)
            ax.text(-0.3, 0.1, f"{180-angle}°", fontsize=12, color='magenta')
            
            ax.set_xlim(-1.2, 1.2)
            ax.set_ylim(-1, 1.2)
            ax.set_aspect('equal')
            ax.grid(True, alpha=0.3)
            ax.set_title("Supplementary Angles (Straight Line = 180°)")
            st.pyplot(fig)
            
            if show_teacher_notes:
                with st.expander("📚 Teacher Notes (Supplementary)"):
                    st.write(
                        "When two angles form a straight line, they are supplementary. "
                        "This is one of the most important angle relationships in Euclidean geometry."
                    )
    
    elif angle_type == "Alternate Angles":
        if st.button("Show alternate angles"):
            st.write("When a transversal crosses two parallel lines, alternate angles are equal.")
            col_l, col_r = st.columns([2, 3])
            with col_l:
                st.latex(r"\text{If lines are parallel:}")
                st.latex(r"\text{Alternate angles are equal}\ (a = c)")
            with col_r:
                st.write("**STEP 0** – Definition of alternate angles on parallel lines.")
            
            col_l, col_r = st.columns([2, 3])
            with col_l:
                st.latex(r"\text{Proof:}\ LP + \text{co-interior} = 180°")
            with col_r:
                st.write("**STEP 1** – Use co-interior angle property to prove.")
            
            if show_teacher_notes:
                with st.expander("📚 Teacher Notes (Alternate Angles)"):
                    st.write(
                        "This is a crucial theorem: when parallel lines are cut by a transversal, "
                        "alternate interior angles are equal. This is used to prove many other theorems."
                    )
    
    elif angle_type == "Angle at Centre":
        if st.button("Show angle property"):
            st.latex(r"\text{Angle at centre}\ =\ 2 \times\ \text{Angle at circumference}")
            col_l, col_r = st.columns([2, 3])
            with col_l:
                st.write("Both angles subtend the **same arc**.")
            with col_r:
                st.write("**STEP 0** – The inscribed angle theorem.")
            
            if show_teacher_notes:
                with st.expander("📚 Teacher Notes (Inscribed Angle)"):
                    st.write(
                        "An angle at the centre is always twice an angle at the circumference "
                        "when they subtend the same arc. This is a fundamental circle theorem."
                    )
    
    if show_quizzes:
        with st.expander("📝 Quiz: Euclidean Geometry"):
            st.write("**Question 1 (1 mark):** If one angle is 60°, what is its supplementary angle?")
            ans1 = st.text_input("Your answer (°)", key="quiz_geo11_1")
            if st.button("Check Q1", key="check_geo11_1"):
                if ans1.strip() == "120":
                    st.success("✓ Correct! 180° − 60° = 120°. **[1 mark]**")
                else:
                    st.error(f"Expected: 120. Your answer: {ans1}")
            
            st.write("**Question 2 (2 marks):** Two parallel lines are cut by a transversal. One alternate angle is 75°. Find the other.")
            ans2 = st.text_input("Your answer (°)", key="quiz_geo11_2")
            if st.button("Check Q2", key="check_geo11_2"):
                if ans2.strip() == "75":
                    st.success("✓ Correct! Alternate angles on parallel lines are equal. **[2 marks]**")
                else:
                    st.error(f"Expected: 75. Your answer: {ans2}")

