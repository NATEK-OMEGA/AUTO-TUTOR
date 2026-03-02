import streamlit as st
import math
from typing import List
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------
# Grade 12 topic handlers with step-by-step pedagogy
# ------------------------------------------

def teach_calculus_differentiation(show_teacher_notes: bool, show_quizzes: bool) -> None:
    st.subheader("Calculus: Differentiation (Grade 12)")
    st.write("Use the power rule to differentiate polynomials and find rates of change.")
    
    st.latex(r"\textbf{Power Rule:}\ \frac{d}{dx}[x^n] = nx^{n-1}")
    
    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input("Coefficient of x^2", value=3.0, format="%.1f")
    with col2:
        b = st.number_input("Coefficient of x", value=5.0, format="%.1f")
    
    if st.button("Differentiate ax² + bx + c"):
        c = st.number_input("Constant term", value=-4.0, format="%.1f")
        
        # STEP 0
        col_l, col_r = st.columns([2, 3])
        with col_l:
            st.latex(rf"\text{{Function:}}\ f(x) = {a}x^2 + {b}x + {c}")
        with col_r:
            st.write("**STEP 0** – Original polynomial function.")
        
        # STEP 1
        col_l, col_r = st.columns([2, 3])
        with col_l:
            st.latex(r"\text{Apply power rule to each term:}")
            st.latex(rf"\frac{{d}}{{dx}}[{a}x^2] = {a} \cdot 2 \cdot x^{{2-1}} = {2*a}x")
            st.latex(rf"\frac{{d}}{{dx}}[{b}x] = {b} \cdot 1 \cdot x^{{1-1}} = {b}")
            st.latex(rf"\frac{{d}}{{dx}}[{c}] = 0")
        with col_r:
            st.write("**STEP 1** – Differentiate each term using the power rule.")
        
        if show_teacher_notes:
            with st.expander("📚 Teacher Notes (Power Rule)"):
                st.write(
                    "The power rule: multiply by the power, reduce power by 1. "
                    "Constant terms become 0. Linear terms become constants."
                )
        
        # STEP 2
        deriv_a = 2 * a
        col_l, col_r = st.columns([2, 3])
        with col_l:
            st.latex(rf"f'(x) = {deriv_a}x + {b}")
        with col_r:
            st.write("**STEP 2** – Combine the differentiated terms to get the derivative.")
        
        if show_teacher_notes:
            with st.expander("📚 Teacher Notes (Interpretation)"):
                st.write(
                    f"f'(x) = {deriv_a}x + {b} tells us the **rate of change** of f at any point x. "
                    f"It's the slope of the tangent line to f(x)."
                )
        
        # STEP 3: Evaluate at a point
        x_eval = st.number_input("Evaluate f'(x) at x =", value=1.0, format="%.1f")
        col_l, col_r = st.columns([2, 3])
        with col_l:
            m_at_x = deriv_a * x_eval + b
            st.latex(rf"f'({x_eval}) = {deriv_a}({x_eval}) + {b} = {m_at_x}")
        with col_r:
            st.write("**STEP 3** – Substitute x-value to find slope at that point.")
        
        st.success(f"✓ **Derivative: f'(x) = {deriv_a}x + {b}**")
        st.info(f"At x = {x_eval}, the slope is {m_at_x:.2f}")
    
    if show_quizzes:
        with st.expander("📝 Quiz: Differentiation"):
            st.write("**Question 1 (2 marks):** Differentiate f(x) = 3x² + 5x − 4.")
            ans1 = st.text_input("Your answer: f'(x) =", key="quiz_diff_1")
            if st.button("Check Q1", key="check_diff_1"):
                if "6x+5" in ans1.replace(" ", "") or "6x + 5" in ans1:
                    st.success("✓ Correct! f'(x) = 6x + 5. **[2 marks]**")
                else:
                    st.error(f"Expected: 6x + 5. Your answer: {ans1}")
            
            st.write("**Question 2 (2 marks):** Differentiate g(x) = 2x³ − 4x + 1.")
            ans2 = st.text_input("Your answer: g'(x) =", key="quiz_diff_2")
            if st.button("Check Q2", key="check_diff_2"):
                if "6x²-4" in ans2.replace(" ", "") or "6x² − 4" in ans2:
                    st.success("✓ Correct! g'(x) = 6x² − 4. **[2 marks]**")
                else:
                    st.error(f"Expected: 6x² − 4. Your answer: {ans2}")


def teach_calculus_integration(show_teacher_notes: bool, show_quizzes: bool) -> None:
    st.subheader("Calculus: Integration (Grade 12)")
    st.write("Find antiderivatives (indefinite integrals) of polynomials.")
    
    st.latex(r"\textbf{Power Rule for Integration:}\ \int x^n \, dx = \frac{x^{n+1}}{n+1} + C")
    
    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input("Coefficient of x^2", value=4.0, format="%.1f")
    with col2:
        b = st.number_input("Coefficient of x", value=3.0, format="%.1f")
    
    if st.button("Integrate ax² + bx + c"):
        c = st.number_input("Constant term", value=2.0, format="%.1f")
        
        # STEP 0
        col_l, col_r = st.columns([2, 3])
        with col_l:
            st.latex(rf"\int ({a}x^2 + {b}x + {c}) \, dx")
        with col_r:
            st.write("**STEP 0** – The integral we need to solve.")
        
        # STEP 1
        col_l, col_r = st.columns([2, 3])
        with col_l:
            st.latex(r"\text{Split into separate integrals:}")
            st.latex(rf"\int {a}x^2 \, dx + \int {b}x \, dx + \int {c} \, dx")
        with col_r:
            st.write("**STEP 1** – Integrate each term separately.")
        
        # STEP 2
        col_l, col_r = st.columns([2, 3])
        with col_l:
            a_coeff = a / 3
            b_coeff = b / 2
            st.latex(rf"\int {a}x^2 \, dx = \frac{{{a}x^3}}{{3}} = {a_coeff:.4f}x^3")
            st.latex(rf"\int {b}x \, dx = \frac{{{b}x^2}}{{2}} = {b_coeff:.4f}x^2")
            st.latex(rf"\int {c} \, dx = {c}x")
        with col_r:
            st.write("**STEP 2** – Apply power rule: add 1 to power, divide by new power.")
        
        if show_teacher_notes:
            with st.expander("📚 Teacher Notes (Integration)"):
                st.write(
                    "Integration is the reverse of differentiation. Always add the constant of integration C "
                    "because the derivative of any constant is 0."
                )
        
        # STEP 3
        col_l, col_r = st.columns([2, 3])
        with col_l:
            st.latex(rf"F(x) = {a_coeff:.4f}x^3 + {b_coeff:.4f}x^2 + {c}x + C")
        with col_r:
            st.write("**STEP 3** – Combine all terms and add constant of integration C.")
        
        st.success(f"✓ **Antiderivative: F(x) = {a_coeff:.4f}x^3 + {b_coeff:.4f}x^2 + {c}x + C**")
    
    if show_quizzes:
        with st.expander("📝 Quiz: Integration"):
            st.write("**Question 1 (2 marks):** Find ∫(4x³) dx.")
            ans1 = st.text_input("Your answer: F(x) =", key="quiz_int_1")
            if st.button("Check Q1", key="check_int_1"):
                if "x^4+C" in ans1.replace(" ", "") or "x⁴+C" in ans1:
                    st.success("✓ Correct! F(x) = x⁴ + C. **[2 marks]**")
                else:
                    st.error(f"Expected: x⁴ + C. Your answer: {ans1}")
            
            st.write("**Question 2 (2 marks):** Find ∫(2x² − 3x + 1) dx.")
            ans2 = st.text_input("Your answer: F(x) =", key="quiz_int_2")
            if st.button("Check Q2", key="check_int_2"):
                if ("⅔x³-1.5x²+x+C" in ans1.replace(" ", "") or 
                    "2/3x³−1.5x²+x+C" in ans2 or
                    "(2/3)x³" in ans2):
                    st.success("✓ Correct! F(x) = (⅔)x³ − 1.5x² + x + C. **[2 marks]**")
                else:
                    st.error("Expected: (2/3)x³ − 1.5x² + x + C")


def teach_trig_identities(show_teacher_notes: bool, show_quizzes: bool) -> None:
    st.subheader("Trigonometric Functions & Identities (Grade 12)")
    st.write("Verify and use fundamental trigonometric identities.")
    
    identity_type = st.radio("Select identity to explore",
                             ["Pythagorean: sin²θ + cos²θ = 1",
                              "Double Angle: sin(2θ) = 2sin(θ)cos(θ)",
                              "Sum Rule: sin(A+B) = ..."])
    
    if identity_type == "Pythagorean: sin²θ + cos²θ = 1":
        angle = st.slider("Choose angle (degrees)", 0, 360, 30)
        if st.button("Verify identity"):
            rad = math.radians(angle)
            sin_val = math.sin(rad)
            cos_val = math.cos(rad)
            sin_sq = sin_val ** 2
            cos_sq = cos_val ** 2
            sum_val = sin_sq + cos_sq
            
            # STEP 0
            col_l, col_r = st.columns([2, 3])
            with col_l:
                st.latex(rf"\text{{Angle}}:\ \theta = {angle}°")
            with col_r:
                st.write("**STEP 0** – Choose an angle to verify the identity.")
            
            # STEP 1
            col_l, col_r = st.columns([2, 3])
            with col_l:
                st.latex(rf"\sin({angle}°) = {sin_val:.6f}")
                st.latex(rf"\cos({angle}°) = {cos_val:.6f}")
            with col_r:
                st.write("**STEP 1** – Calculate sin(θ) and cos(θ).")
            
            # STEP 2
            col_l, col_r = st.columns([2, 3])
            with col_l:
                st.latex(rf"\sin^2({angle}°) = ({sin_val:.6f})^2 = {sin_sq:.6f}")
                st.latex(rf"\cos^2({angle}°) = ({cos_val:.6f})^2 = {cos_sq:.6f}")
            with col_r:
                st.write("**STEP 2** – Square both values.")
            
            # STEP 3
            col_l, col_r = st.columns([2, 3])
            with col_l:
                st.latex(rf"\sin^2({angle}°) + \cos^2({angle}°) = {sin_sq:.6f} + {cos_sq:.6f} = {sum_val:.6f}")
            with col_r:
                st.write("**STEP 3** – Add them together.")
            
            # STEP 4
            col_l, col_r = st.columns([2, 3])
            with col_l:
                st.latex(rf"{sum_val:.6f} \approx 1\ \checkmark")
            with col_r:
                st.write("**STEP 4** – Verify they sum to 1 (within rounding error).")
            
            if show_teacher_notes:
                with st.expander("📚 Teacher Notes (Pythagorean Identity)"):
                    st.write(
                        "This fundamental identity follows from the unit circle definition. "
                        "sin²θ + cos²θ = 1 is true for ALL angles, not just specific ones. "
                        "Use it to simplify trigonometric expressions and prove other identities."
                    )
    
    elif identity_type == "Double Angle: sin(2θ) = 2sin(θ)cos(θ)":
        angle = st.slider("Choose angle (degrees)", 0, 180, 30)
        if st.button("Verify double angle"):
            rad = math.radians(angle)
            rad2 = 2 * rad
            sin_val = math.sin(rad)
            cos_val = math.cos(rad)
            sin_2_formula = 2 * sin_val * cos_val
            sin_2_direct = math.sin(rad2)
            
            col_l, col_r = st.columns([2, 3])
            with col_l:
                st.latex(rf"\text{{LHS:}}\ \sin(2 \times {angle}°) = \sin({2*angle}°) = {sin_2_direct:.6f}")
            with col_r:
                st.write("**STEP 1** – Calculate sin(2θ) directly.")
            
            col_l, col_r = st.columns([2, 3])
            with col_l:
                st.latex(rf"\text{{RHS:}}\ 2\sin({angle}°)\cos({angle}°) = 2 \times {sin_val:.6f} \times {cos_val:.6f} = {sin_2_formula:.6f}")
            with col_r:
                st.write("**STEP 2** – Calculate 2sin(θ)cos(θ).")
            
            col_l, col_r = st.columns([2, 3])
            with col_l:
                if abs(sin_2_direct - sin_2_formula) < 1e-5:
                    st.latex(rf"{sin_2_direct:.6f} = {sin_2_formula:.6f}\ \checkmark")
            with col_r:
                st.write("**STEP 3** – Both sides are equal!")
    
    if show_quizzes:
        with st.expander("📝 Quiz: Trigonometric Identities"):
            st.write("**Question 1 (1 mark):** Simplify sin²(45°) + cos²(45°).")
            ans1 = st.text_input("Your answer", key="quiz_id_1")
            if st.button("Check Q1", key="check_id_1"):
                if ans1.strip() == "1":
                    st.success("✓ Correct! sin²(45°) + cos²(45°) = 1. **[1 mark]**")
                else:
                    st.error(f"Expected: 1. Your answer: {ans1}")
            
            st.write("**Question 2 (2 marks):** Find sin(60°) using the identity sin²(60°) + cos²(60°) = 1 and the fact that cos(60°) = 0.5.")
            ans2 = st.text_input("Your answer (decimal)", key="quiz_id_2")
            if st.button("Check Q2", key="check_id_2"):
                # sin²(60°) = 1 - 0.25 = 0.75, so sin(60°) ≈ 0.866
                try:
                    user_val = float(ans2.strip())
                    if abs(user_val - 0.866) < 0.01:
                        st.success("✓ Correct! sin(60°) ≈ 0.866 or √3/2. **[2 marks]**")
                    else:
                        st.error("Expected: ≈0.866 (or √3/2)")
                except ValueError:
                    st.error("Please enter a number.")


def teach_analytic_geometry(show_teacher_notes: bool, show_quizzes: bool) -> None:
    st.subheader("Analytic Geometry (Grade 12)")
    st.write("Investigate circles and their equations in the coordinate plane.")
    
    col1, col2 = st.columns(2)
    with col1:
        h = st.number_input("Centre x-coordinate (h)", value=0.0, format="%.1f")
    with col2:
        k = st.number_input("Centre y-coordinate (k)", value=0.0, format="%.1f")
    
    if st.button("Explore circle"):
        r = st.number_input("Radius (r)", value=3.0, format="%.1f")
        
        # STEP 0
        col_l, col_r = st.columns([2, 3])
        with col_l:
            st.latex(rf"\text{{Circle centred at}}\ ({h}, {k})\ \text{{with radius}}\ {r}")
        with col_r:
            st.write("**STEP 0** – Circle parameters.")
        
        # STEP 1
        col_l, col_r = st.columns([2, 3])
        with col_l:
            st.latex(rf"\textbf{{Standard form:}}\ (x - {h})^2 + (y - {k})^2 = {r}^2")
            st.latex(rf"(x - {h})^2 + (y - {k})^2 = {r**2}")
        with col_r:
            st.write("**STEP 1** – Write equation in standard form.")
        
        if show_teacher_notes:
            with st.expander("📚 Teacher Notes (Circle Equation)"):
                st.write(
                    f"The general circle equation: **(x − h)² + (y − k)² = r²**\\n"
                    f"This comes from the distance formula: distance from (x,y) to centre (h,k) equals r."
                )
        
        # STEP 2: Check a point
        test_x = st.number_input("Test x-coordinate", value=h+r, format="%.1f")
        col_l, col_r = st.columns([2, 3])
        with col_l:
            dist_sq = (test_x - h)**2 + (0 - k)**2
            st.latex(rf"\text{{Point}}\ ({test_x}, 0):")
            st.latex(rf"({test_x} - {h})^2 + (0 - {k})^2 = {(test_x-h)**2} + {(0-k)**2} = {dist_sq}")
        with col_r:
            st.write("**STEP 2** – Check if point lies on circle.")
            if abs(dist_sq - r**2) < 0.01:
                st.write("✓ Point is ON the circle!")
            else:
                st.write(f"✗ Point is NOT on circle (need {r**2})")
        
        # STEP 3: Plot
        fig, ax = plt.subplots(figsize=(8, 8))
        theta = np.linspace(0, 2*np.pi, 200)
        x_circle = h + r * np.cos(theta)
        y_circle = k + r * np.sin(theta)
        r_sq = r ** 2
        ax.plot(x_circle, y_circle, 'b-', linewidth=2, label=f'Circle: (x-{h})² + (y-{k})² = {r_sq}')
        ax.plot(h, k, 'ro', markersize=8, label=f'Centre ({h}, {k})')
        ax.axhline(y=0, color='k', linewidth=0.5)
        ax.axvline(x=0, color='k', linewidth=0.5)
        ax.grid(True, alpha=0.3)
        ax.set_aspect('equal')
        ax.legend()
        ax.set_title(f'Circle centred at ({h}, {k}) with radius {r}')
        st.pyplot(fig)
    
    if show_quizzes:
        with st.expander("📝 Quiz: Analytic Geometry"):
            st.write("**Question 1 (1 mark):** What is the radius of circle x² + y² = 25?")
            ans1 = st.text_input("Your answer", key="quiz_ag_1")
            if st.button("Check Q1", key="check_ag_1"):
                if ans1.strip() == "5":
                    st.success("✓ Correct! r = √25 = 5. **[1 mark]**")
                else:
                    st.error(f"Expected: 5. Your answer: {ans1}")
            
            st.write("**Question 2 (2 marks):** Write the equation of a circle centred at (2, −3) with radius 4.")
            ans2 = st.text_input("Your answer: (x...)", key="quiz_ag_2")
            if st.button("Check Q2", key="check_ag_2"):
                if ("(x-2)²+(y+3)²=16" in ans2.replace(" ", "") or
                    "(x−2)²+(y+3)²=16" in ans2):
                    st.success("✓ Correct! (x−2)² + (y+3)² = 16. **[2 marks]**")
                else:
                    st.error("Expected: (x−2)² + (y+3)² = 16")


def teach_probability_statistics(show_teacher_notes: bool, show_quizzes: bool) -> None:
    # Reuse Grade 10 implementation for Grade 12
    from topics.grade10 import teach_probability_statistics as base_stats
    base_stats(show_teacher_notes, show_quizzes)


def teach_finance(show_teacher_notes: bool, show_quizzes: bool) -> None:
    # Reuse Grade 10 implementation for Grade 12
    from topics.grade10 import teach_finance as base_fin
    base_fin(show_teacher_notes, show_quizzes)
