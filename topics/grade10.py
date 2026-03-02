import streamlit as st
import math
from typing import List
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# ------------------------------------------
# Grade 10 topic handlers with step-by-step pedagogy
# ------------------------------------------

def teach_numbers_patterns(show_teacher_notes: bool, show_quizzes: bool) -> None:
    st.subheader("Numbers & Patterns (Grade 10)")
    st.write(
        "Identify arithmetic and geometric sequences by analysing first differences and ratios."
    )
    seq_str = st.text_input("Enter sequence terms (comma separated)", "2,5,8,11")
    if st.button("Analyse sequence"):
        try:
            seq = [float(x.strip()) for x in seq_str.split(",") if x.strip()]
            if len(seq) < 2:
                st.error("Need at least two terms to analyse.")
            else:
                # STEP 0: Display input
                col_l, col_r = st.columns([2, 3])
                with col_l:
                    st.latex(r"\textbf{Given\ sequence:}\ " + ", ".join(str(int(x) if x==int(x) else x) for x in seq))
                with col_r:
                    st.write("**STEP 0** – Display the given sequence.")
                
                # STEP 1: Calculate first differences
                diffs = [seq[i+1]-seq[i] for i in range(len(seq)-1)]
                col_l, col_r = st.columns([2, 3])
                with col_l:
                    calc_details = [f"{seq[i+1]} - {seq[i]} = {diffs[i]}" for i in range(len(seq)-1)]
                    st.latex(r"\textbf{First\ differences:}\ " + ", ".join(str(int(d) if d==int(d) else d) for d in diffs))
                    st.write("Calculations: " + " | ".join(calc_details[:3]) + ("..." if len(calc_details) > 3 else ""))
                with col_r:
                    st.write("**STEP 1** – Subtract each term from the next term.")
                
                if show_teacher_notes:
                    with st.expander("📚 Teacher Notes (STEP 1)"):
                        st.write(
                            "First differences show how the sequence changes from term to term. If all differences are equal, "
                            "the sequence increases at a constant rate, which indicates an **arithmetic sequence**."
                        )
                
                # STEP 2: Check if constant
                all_equal = all(abs(diffs[i]-diffs[0])<1e-6 for i in range(len(diffs)))
                col_l, col_r = st.columns([2, 3])
                with col_l:
                    if all_equal:
                        st.latex(r"\text{All differences equal?}\ \checkmark")
                    else:
                        st.latex(r"\text{All differences equal?}\ \times")
                with col_r:
                    st.write("**STEP 2** – Check if all first differences are equal.")
                
                if all_equal:
                    col_l, col_r = st.columns([2, 3])
                    with col_l:
                        d_val = diffs[0]
                        st.success(f"✓ **ARITHMETIC SEQUENCE** with common difference d = {int(d_val) if d_val==int(d_val) else d_val}")
                    with col_r:
                        st.write("**STEP 3** – Conclusion: Equal differences identify arithmetic sequence.")
                    
                    if show_teacher_notes:
                        with st.expander("📚 Teacher Notes (Arithmetic Sequence)"):
                            st.write(
                                f"Formula: **T(n) = a + (n−1)d** where a = {seq[0]} and d = {diffs[0]}\\n"
                                f"For this sequence: T(n) = {seq[0]} + (n−1)×{diffs[0]}\\n"
                                f"Use this to find any term directly without listing all previous terms!"
                            )
                else:
                    # Check geometric
                    ratios = []
                    for i in range(len(seq)-1):
                        if seq[i] != 0:
                            ratios.append(seq[i+1]/seq[i])
                    
                    col_l, col_r = st.columns([2, 3])
                    with col_l:
                        st.latex(r"\text{Calculate ratios:}\ " + ", ".join(f"{r:.3f}" for r in ratios[:min(3, len(ratios))]))
                    with col_r:
                        st.write("**STEP 3** – Divide each term by the previous term to find ratio.")
                    
                    if ratios and all(abs(r - ratios[0]) < 1e-6 for r in ratios):
                        col_l, col_r = st.columns([2, 3])
                        with col_l:
                            st.success(f"✓ **GEOMETRIC SEQUENCE** with ratio r = {ratios[0]:.4f}")
                        with col_r:
                            st.write("**STEP 4** – Equal ratios identify geometric sequence.")
                        
                        if show_teacher_notes:
                            with st.expander("📚 Teacher Notes (Geometric Sequence)"):
                                st.write(
                                    f"Formula: **T(n) = a·r^(n−1)** where a = {seq[0]} and r = {ratios[0]:.4f}\\n"
                                    f"Geometric sequences grow/decay exponentially, not linearly."
                                )
                    else:
                        col_l, col_r = st.columns([2, 3])
                        with col_l:
                            st.info("? Neither constant differences nor constant ratio")
                        with col_r:
                            st.write("**STEP 4** – Sequence type: Other (possibly quadratic or custom pattern).")
        except ValueError:
            st.error("Could not parse sequence. Use numbers separated by commas.")
    
    if show_quizzes:
        with st.expander("📝 Quiz: Sequence Analysis"):
            st.write("**Question 1 (2 marks):** The sequence 4, 7, 10, 13 is arithmetic. What is the common difference?")
            ans1 = st.text_input("Your answer", key="quiz_np_1")
            if st.button("Check Q1", key="check_np_1"):
                if ans1.strip() == "3":
                    st.success("✓ Correct! 7−4=3, 10−7=3, etc. **[2 marks]**")
                else:
                    st.error(f"Expected: 3. Your answer: {ans1}")
            
            st.write("**Question 2 (3 marks):** Find the 5th term of the arithmetic sequence 2, 5, 8, 11, ...\\nUse T(n) = a + (n−1)d")
            ans2 = st.text_input("Your answer", key="quiz_np_2")
            if st.button("Check Q2", key="check_np_2"):
                if ans2.strip() == "14":
                    st.success("✓ Correct! T(5) = 2 + (5−1)×3 = 2 + 12 = 14. **[3 marks]**")
                else:
                    st.error(f"Expected: 14. Your answer: {ans2}")



def teach_algebra_expressions(show_teacher_notes: bool, show_quizzes: bool) -> None:
    st.subheader("Algebra: Expressions & Equations (Grade 10)")
    st.write("Solve linear equations of the form ax + b = c using the balance method (inverse operations).")
    
    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input("Coefficient a", value=2.0, format="%.1f")
    with col2:
        b = st.number_input("Constant b", value=-8.0, format="%.1f")
    
    if st.button("Solve equation"):
        if abs(a) < 1e-9:
            st.error("Coefficient a cannot be zero.")
        else:
            # STEP 0: Display equation
            col_l, col_r = st.columns([2, 3])
            with col_l:
                if b >= 0:
                    st.latex(rf"{a}x + {b} = 0")
                else:
                    st.latex(rf"{a}x - {abs(b)} = 0")
            with col_r:
                st.write("**STEP 0** – The equation we need to solve.")
            
            if show_teacher_notes:
                with st.expander("📚 Teacher Notes (Equation Setup)"):
                    st.write("The goal is to isolate x. We use **inverse operations** (opposite operations) to undo each step.")
            
            # STEP 1: Add/subtract b
            col_l, col_r = st.columns([2, 3])
            with col_l:
                opposite_b = -b
                if b >= 0:
                    st.latex(rf"{a}x + {b} \textcolor{{red}}{{-({b})}} = 0 \textcolor{{red}}{{-({b})}}")
                    st.latex(rf"{a}x = {opposite_b}")
                else:
                    st.latex(rf"{a}x - {abs(b)} \textcolor{{red}}{{+{abs(b)}}} = 0 \textcolor{{red}}{{+{abs(b)}}}")
                    st.latex(rf"{a}x = {opposite_b}")
            with col_r:
                st.write("**STEP 1** – Subtract " + str(b) + " from both sides (balance method).")
            
            if show_teacher_notes:
                with st.expander("📚 Teacher Notes (STEP 1)"):
                    st.write(
                        "**The Balance Method:** Whatever operation we do to one side, we must do to the other. "
                        "We subtract b to eliminate the constant term and isolate the x term."
                    )
            
            # STEP 2: Divide by a
            x_val = -b / a
            col_l, col_r = st.columns([2, 3])
            with col_l:
                st.latex(rf"\frac{{{a}x}}{{\textcolor{{red}}{{{a}}}}} = \frac{{{opposite_b}}}{{\textcolor{{red}}{{{a}}}}}")
                st.latex(rf"x = \frac{{{opposite_b}}}{{{a}}} = {x_val}")
            with col_r:
                st.write(f"**STEP 2** – Divide both sides by {a} (inverse of multiplication).")
            
            if show_teacher_notes:
                with st.expander("📚 Teacher Notes (STEP 2)"):
                    st.write(
                        "Dividing by the coefficient isolates x. This is the inverse of multiplication. "
                        "Now x stands alone and we have our solution."
                    )
            
            # STEP 3: Verify
            check_val = a * x_val + b
            col_l, col_r = st.columns([2, 3])
            with col_l:
                st.latex(rf"\textbf{{Verify:}}\ {a}({x_val}) + {b} = {check_val:.6f} \approx 0\ \checkmark")
            with col_r:
                st.write("**STEP 3** – Check: substitute x back into the original equation.")
            
            if show_teacher_notes:
                with st.expander("📚 Teacher Notes (Verification)"):
                    st.write(
                        "Always verify your solution! Substitute back into the original equation. "
                        "If LHS = RHS, your solution is correct."
                    )
            
            st.markdown("---")
            st.success(f"✓ **Solution: x = {x_val}**")
    
    if show_quizzes:
        with st.expander("📝 Quiz: Solve Equations"):
            st.write("**Question 1 (2 marks):** Solve 3x + 6 = 0 for x.")
            ans1 = st.text_input("Your answer", key="quiz_alg_1")
            if st.button("Check Q1", key="check_alg_1"):
                if ans1.strip() == "-2" or ans1.strip() == "−2":
                    st.success("✓ Correct! 3x = −6, so x = −2. **[2 marks]**")
                else:
                    st.error(f"Expected: -2. Your answer: {ans1}")
            
            st.write("**Question 2 (3 marks):** Solve 5x − 15 = 0. Show all steps.")
            ans2 = st.text_input("Your answer", key="quiz_alg_2")
            if st.button("Check Q2", key="check_alg_2"):
                if ans2.strip() == "3":
                    st.success("✓ Correct! 5x = 15, x = 3. **[3 marks]**")
                else:
                    st.error(f"Expected: 3. Your answer: {ans2}")


def teach_finance(show_teacher_notes: bool, show_quizzes: bool) -> None:
    st.subheader("Finance Mathematics")
    st.write("Calculate simple and compound interest step-by-step using CAPS formulas.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        P = st.number_input("Principal (R)", value=1000.0, format="%.2f")
    with col2:
        r = st.number_input("Annual rate (%)", value=5.0, format="%.1f")
    with col3:
        t = st.number_input("Time (years)", value=2.0, format="%.1f")
    
    if st.button("Calculate interest"):
        st.subheader("Simple Interest")
        
        # STEP 0
        col_l, col_r = st.columns([2, 3])
        with col_l:
            st.latex(r"\textbf{Formula:}\ SI = \frac{P \times r \times t}{100}")
        with col_r:
            st.write("**STEP 0** – Simple Interest formula (South African CAPS).")
        
        # STEP 1
        col_l, col_r = st.columns([2, 3])
        with col_l:
            st.latex(rf"SI = \frac{{{P} \times {r} \times {t}}}{{100}}")
        with col_r:
            st.write("**STEP 1** – Substitute P, r, and t into the formula.")
        
        # STEP 2
        numerator = P * r * t
        col_l, col_r = st.columns([2, 3])
        with col_l:
            st.latex(rf"SI = \frac{{{numerator}}}{{100}}")
        with col_r:
            st.write("**STEP 2** – Multiply in the numerator: " + f"{P} × {r} × {t} = {numerator}")
        
        # STEP 3
        si = numerator / 100
        col_l, col_r = st.columns([2, 3])
        with col_l:
            st.latex(rf"SI = {si:.2f}")
        with col_r:
            st.write("**STEP 3** – Divide by 100 to get the interest earned.")
        
        # STEP 4
        amount_si = P + si
        col_l, col_r = st.columns([2, 3])
        with col_l:
            st.latex(rf"\text{{Total Amount}} = P + SI = {P} + {si:.2f} = {amount_si:.2f}")
        with col_r:
            st.write("**STEP 4** – Add interest to principal for total amount.")
        
        if show_teacher_notes:
            with st.expander("📚 Teacher Notes (Simple Interest)"):
                st.write(
                    "Simple interest is fixed: the same amount is earned each year. "
                    "Interest = Principal × Rate × Time ÷ 100. This is a **linear** growth model."
                )
        
        st.success(f"✓ Simple Interest earned: **R{si:.2f}** | Total: **R{amount_si:.2f}**")
        
        st.markdown("---")
        st.subheader("Compound Interest")
        
        # STEP 0
        col_l, col_r = st.columns([2, 3])
        with col_l:
            st.latex(r"\textbf{Formula:}\ A = P \left(1 + \frac{r}{100}\right)^t")
        with col_r:
            st.write("**STEP 0** – Compound Interest formula (interest on interest).")
        
        # STEP 1
        interior = 1 + r/100
        col_l, col_r = st.columns([2, 3])
        with col_l:
            st.latex(rf"A = {P} \times \left(1 + \frac{{{r}}}{{100}}\right)^{{{t}}}")
        with col_r:
            st.write("**STEP 1** – Substitute P, r, t into the formula.")
        
        # STEP 2
        col_l, col_r = st.columns([2, 3])
        with col_l:
            st.latex(rf"1 + \frac{{{r}}}{{100}} = 1 + {r/100:.4f} = {interior:.4f}")
        with col_r:
            st.write("**STEP 2** – Compute the growth factor (1 + r/100).")
        
        # STEP 3
        growth_factor = interior ** t
        col_l, col_r = st.columns([2, 3])
        with col_l:
            st.latex(rf"({interior:.4f})^{{{t}}} = {growth_factor:.6f}")
        with col_r:
            st.write(f"**STEP 3** – Raise growth factor to power {t}.")
        
        # STEP 4
        amount_ci = P * growth_factor
        col_l, col_r = st.columns([2, 3])
        with col_l:
            st.latex(rf"A = {P} \times {growth_factor:.6f} = {amount_ci:.2f}")
        with col_r:
            st.write("**STEP 4** – Multiply principal by growth factor.")
        
        # STEP 5
        ci_earned = amount_ci - P
        col_l, col_r = st.columns([2, 3])
        with col_l:
            st.latex(rf"\text{{Interest earned}} = {amount_ci:.2f} - {P} = {ci_earned:.2f}")
        with col_r:
            st.write("**STEP 5** – Interest = Total Amount − Principal")
        
        if show_teacher_notes:
            with st.expander("📚 Teacher Notes (Compound Interest)"):
                st.write(
                    "Compound interest earns 'interest on interest' because each period the interest is added "
                    "to the principal, and the next interest is calculated on this new amount. "
                    "This creates **exponential** growth—much faster than simple interest over long periods!"
                )
        
        st.success(f"✓ Compound Interest earned: **R{ci_earned:.2f}** | Total: **R{amount_ci:.2f}**")
        
        # Comparison
        st.markdown("---")
        st.subheader("Comparison")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Simple Interest", f"R{si:.2f}")
        with col2:
            st.metric("Compound Interest", f"R{ci_earned:.2f}")
        with col3:
            st.metric("Difference", f"R{ci_earned - si:.2f}")
    
    if show_quizzes:
        with st.expander("📝 Quiz: Finance Mathematics"):
            st.write("**Question 1 (2 marks):** Find the simple interest on R5000 at 4% p.a. for 3 years.")
            ans1 = st.text_input("Interest earned (R)", key="quiz_fin_1")
            if st.button("Check Q1", key="check_fin_1"):
                expected = 5000 * 4 / 100 * 3
                try:
                    user_val = float(ans1.strip())
                    if abs(user_val - expected) < 0.01:
                        st.success(f"✓ Correct! R{expected:.2f}. **[2 marks]**")
                    else:
                        st.error(f"Expected: R{expected:.2f}, You entered: R{user_val:.2f}")
                except ValueError:
                    st.error("Please enter a number.")
            
            st.write("**Question 2 (3 marks):** R2000 is invested at 6% p.a. compound interest for 2 years. What is the total amount?")
            ans2 = st.text_input("Total amount (R)", key="quiz_fin_2")
            if st.button("Check Q2", key="check_fin_2"):
                expected = 2000 * ((1 + 6/100) ** 2)
                try:
                    user_val = float(ans2.strip())
                    if abs(user_val - expected) < 0.50:
                        st.success(f"✓ Correct! R{expected:.2f}. **[3 marks]**")
                    else:
                        st.error(f"Expected: R{expected:.2f}, You entered: R{user_val:.2f}")
                except ValueError:
                    st.error("Please enter a number.")


def teach_measurement_geometry(show_teacher_notes: bool, show_quizzes: bool) -> None:
    st.subheader("Measurement & Geometry (Grade 10)")
    st.write("Calculate area and perimeter of common shapes step-by-step.")
    
    shape = st.selectbox("Select a shape", ["Rectangle", "Circle", "Triangle"])
    
    if shape == "Rectangle":
        st.subheader("Rectangle")
        col1, col2 = st.columns(2)
        with col1:
            w = st.number_input("Width (m)", value=5.0, format="%.1f")
        with col2:
            h = st.number_input("Height (m)", value=3.0, format="%.1f")
        
        if st.button("Calculate"):
            # Area
            col_l, col_r = st.columns([2, 3])
            with col_l:
                st.latex(r"\textbf{Area} = \text{length} \times \text{width}")
            with col_r:
                st.write("**STEP 0** – Area formula for rectangle.")
            
            area = w * h
            col_l, col_r = st.columns([2, 3])
            with col_l:
                st.latex(rf"\text{{Area}} = {w} \times {h} = {area}")
            with col_r:
                st.write("**STEP 1** – Multiply width by height.")
            
            # Perimeter
            col_l, col_r = st.columns([2, 3])
            with col_l:
                st.latex(r"\textbf{Perimeter} = 2(\text{length} + \text{width})")
            with col_r:
                st.write("**STEP 2** – Perimeter formula for rectangle.")
            
            perimeter = 2 * (w + h)
            col_l, col_r = st.columns([2, 3])
            with col_l:
                st.latex(rf"\text{{Perimeter}} = 2({w} + {h}) = 2 \times {w+h} = {perimeter}")
            with col_r:
                st.write("**STEP 3** – Add dimensions, then multiply by 2.")
            
            if show_teacher_notes:
                with st.expander("📚 Teacher Notes (Rectangle)"):
                    st.write(
                        "**Area** measures the 2D space inside. **Perimeter** measures the distance around the edge. "
                        "Always include units (m², m, cm², cm, etc.)."
                    )
            
            st.success(f"✓ Area = **{area:.2f} m²** | Perimeter = **{perimeter:.2f} m**")
    
    elif shape == "Circle":
        st.subheader("Circle")
        r = st.number_input("Radius (m)", value=3.0, format="%.1f")
        
        if st.button("Calculate"):
            # Area
            col_l, col_r = st.columns([2, 3])
            with col_l:
                st.latex(r"\textbf{Area} = \pi r^2")
            with col_r:
                st.write("**STEP 0** – Area formula: π times radius squared.")
            
            area = math.pi * r * r
            col_l, col_r = st.columns([2, 3])
            with col_l:
                st.latex(rf"\text{{Area}} = \pi \times {r}^2 = {r**2}\pi \approx {area:.2f}")
            with col_r:
                st.write("**STEP 1** – Square the radius, multiply by π (≈3.14159).")
            
            # Circumference
            col_l, col_r = st.columns([2, 3])
            with col_l:
                st.latex(r"\textbf{Circumference} = 2\pi r")
            with col_r:
                st.write("**STEP 2** – Circumference formula: 2π times radius.")
            
            circum = 2 * math.pi * r
            col_l, col_r = st.columns([2, 3])
            with col_l:
                st.latex(rf"\text{{Circumference}} = 2\pi \times {r} = {2*r}\pi \approx {circum:.2f}")
            with col_r:
                st.write("**STEP 3** – Multiply radius by 2, then by π.")
            
            if show_teacher_notes:
                with st.expander("📚 Teacher Notes (Circle)"):
                    st.write(
                        "**π (pi)** is the ratio of circumference to diameter. It appears in all circle formulas. "
                        "In Grade 10 onwards, use π values from your calculator for accuracy."
                    )
            
            fig, ax = plt.subplots(figsize=(6, 6))
            circle = patches.Circle((0.5, 0.5), 0.3, fill=False, edgecolor='blue', linewidth=2)
            ax.add_patch(circle)
            ax.plot([0.5, 0.8], [0.5, 0.5], 'r-', linewidth=2, label=f'Radius = {r}m')
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.set_aspect('equal')
            ax.legend()
            ax.set_title(f"Circle with radius {r}m")
            st.pyplot(fig)
            
            st.success(f"✓ Area = **{area:.2f} m²** | Circumference = **{circum:.2f} m**")
    
    else:  # Triangle
        st.subheader("Triangle")
        col1, col2 = st.columns(2)
        with col1:
            base = st.number_input("Base (m)", value=6.0, format="%.1f")
        with col2:
            height = st.number_input("Height (m)", value=4.0, format="%.1f")
        
        if st.button("Calculate"):
            col_l, col_r = st.columns([2, 3])
            with col_l:
                st.latex(r"\textbf{Area} = \frac{1}{2} \times \text{base} \times \text{height}")
            with col_r:
                st.write("**STEP 0** – Triangle area formula.")
            
            area = 0.5 * base * height
            col_l, col_r = st.columns([2, 3])
            with col_l:
                st.latex(rf"\text{{Area}} = \frac{{1}}{{2}} \times {base} \times {height} = \frac{{{base*height}}}{{2}} = {area}")
            with col_r:
                st.write("**STEP 1** – Multiply base and height, then divide by 2.")
            
            if show_teacher_notes:
                with st.expander("📚 Teacher Notes (Triangle)"):
                    st.write(
                        "A triangle is half a rectangle. If a rectangle has area = base × height, "
                        "then a triangle with the same base and height is half that: ½ × base × height."
                    )
            
            st.success(f"✓ Area = **{area:.2f} m²**")
    
    if show_quizzes:
        with st.expander("📝 Quiz: Measurement"):
            st.write("**Question 1 (2 marks):** Find the area of a rectangle with sides 5 m and 7 m.")
            ans1 = st.text_input("Area (m²)", key="quiz_geo_1")
            if st.button("Check Q1", key="check_geo_1"):
                if ans1.strip() == "35":
                    st.success("✓ Correct! 5 × 7 = 35 m². **[2 marks]**")
                else:
                    st.error(f"Expected: 35. Your answer: {ans1}")
            
            st.write("**Question 2 (3 marks):** What is the circumference of a circle with radius 5 m? (Use π ≈ 3.14)")
            ans2 = st.text_input("Circumference (m)", key="quiz_geo_2")
            if st.button("Check Q2", key="check_geo_2"):
                expected = 2 * 3.14 * 5
                try:
                    user_val = float(ans2.strip())
                    if abs(user_val - expected) < 0.5:
                        st.success(f"✓ Correct! ≈{expected:.1f} m. **[3 marks]**")
                    else:
                        st.error(f"Expected: ≈{expected:.1f} m. Your answer: {user_val:.1f} m")
                except ValueError:
                    st.error("Please enter a number.")


def teach_trigonometry(show_teacher_notes: bool, show_quizzes: bool) -> None:
    st.subheader("Trigonometry (Grade 10)")
    st.write("Evaluate trigonometric ratios for acute angles in right-angled triangles.")
    
    angle = st.slider("Select angle (degrees)", 0, 90, 30)
    rad = math.radians(angle)
    
    if st.button("Evaluate trig ratios"):
        # STEP 0: Show unit circle concept
        col_l, col_r = st.columns([2, 3])
        with col_l:
            st.latex(r"\textbf{Angle} = " + str(angle) + r"°")
        with col_r:
            st.write("**STEP 0** – Select an angle on the unit circle.")
        
        # STEP 1: Calculate sine
        sin_val = math.sin(rad)
        col_l, col_r = st.columns([2, 3])
        with col_l:
            st.latex(rf"\sin({angle}°) = {sin_val:.4f}")
        with col_r:
            st.write("**STEP 1** – Sine = opposite ÷ hypotenuse (y-coordinate on unit circle).")
        
        # STEP 2: Calculate cosine
        cos_val = math.cos(rad)
        col_l, col_r = st.columns([2, 3])
        with col_l:
            st.latex(rf"\cos({angle}°) = {cos_val:.4f}")
        with col_r:
            st.write("**STEP 2** – Cosine = adjacent ÷ hypotenuse (x-coordinate on unit circle).")
        
        # STEP 3: Calculate tangent
        if abs(cos_val) > 1e-9:
            tan_val = math.tan(rad)
            col_l, col_r = st.columns([2, 3])
            with col_l:
                st.latex(rf"\tan({angle}°) = \frac{{\sin({angle}°)}}{{\cos({angle}°)}} = {tan_val:.4f}")
            with col_r:
                st.write("**STEP 3** – Tangent = sin ÷ cos = opposite ÷ adjacent.")
        
        if show_teacher_notes:
            with st.expander("📚 Teacher Notes (Trig Ratios)"):
                st.write(
                    "**SOH-CAH-TOA** memory aid:\\n"
                    "- **Sine** = Opposite ÷ Hypotenuse\\n"
                    "- **Cosine** = Adjacent ÷ Hypotenuse\\n"
                    "- **Tangent** = Opposite ÷ Adjacent\\n"
                    "These ratios are properties of the angle, not the triangle size!"
                )
        
        # Draw unit circle
        fig, ax = plt.subplots(figsize=(6, 6))
        theta = np.linspace(0, 2*np.pi, 100)
        ax.plot(np.cos(theta), np.sin(theta), 'b-', linewidth=1)
        
        # Draw angle
        angle_rad = math.radians(angle)
        ax.plot([0, np.cos(angle_rad)], [0, np.sin(angle_rad)], 'r-', linewidth=2, label=f'{angle}°')
        ax.plot([np.cos(angle_rad), np.cos(angle_rad)], [0, np.sin(angle_rad)], 'g--', linewidth=1, label='sin')
        ax.plot([0, np.cos(angle_rad)], [0, 0], 'g--', linewidth=1, label='cos')
        
        ax.set_xlim(-1.3, 1.3)
        ax.set_ylim(-1.3, 1.3)
        ax.set_aspect('equal')
        ax.axhline(y=0, color='k', linewidth=0.5)
        ax.axvline(x=0, color='k', linewidth=0.5)
        ax.grid(True, alpha=0.3)
        ax.legend()
        ax.set_title("Unit Circle - Trigonometric Ratios")
        st.pyplot(fig)
        
        if show_teacher_notes:
            with st.expander("📚 Teacher Notes (Unit Circle)"):
                st.write(
                    "The **unit circle** has radius 1 centred at the origin. Any angle creates a point on the circle. "
                    "The x-coordinate is cos(θ), the y-coordinate is sin(θ). This is how we define trig for all angles!"
                )
    
    if show_quizzes:
        with st.expander("📝 Quiz: Trigonometry"):
            st.write("**Question 1 (1 mark):** sin(30°) = ?")
            ans1 = st.text_input("Your answer (decimal or fraction 1/2)", key="quiz_trig_1")
            if st.button("Check Q1", key="check_trig_1"):
                if ans1.strip() in ["0.5", "1/2", "0,5"]:
                    st.success("✓ Correct! **[1 mark]**")
                else:
                    st.error("Expected: 0.5 (or 1/2)")
            
            st.write("**Question 2 (2 marks):** In a right triangle, the opposite side = 3m and hypotenuse = 5m. Find sin(θ).")
            ans2 = st.text_input("Your answer (decimal or fraction)", key="quiz_trig_2")
            if st.button("Check Q2", key="check_trig_2"):
                if ans2.strip() in ["0.6", "3/5"]:
                    st.success("✓ Correct! sin(θ) = 3/5 = 0.6. **[2 marks]**")
                else:
                    st.error("Expected: 0.6 (or 3/5)")


def teach_probability_statistics(show_teacher_notes: bool, show_quizzes: bool) -> None:
    st.subheader("Probability & Statistics (Grade 10)")
    st.write("Calculate measures of central tendency and spread.")
    
    data_str = st.text_input("Enter data values (comma separated)", "5,3,8,3,10,5,8,5")
    
    if st.button("Analyse data"):
        try:
            data = [float(x.strip()) for x in data_str.split(",") if x.strip()]
            if len(data) < 1:
                st.error("Need at least one data value.")
            else:
                # STEP 0: Display data
                col_l, col_r = st.columns([2, 3])
                with col_l:
                    st.write(f"**Data:** {data}")
                with col_r:
                    st.write("**STEP 0** – Organize the given data set.")
                
                # STEP 1: Find mean
                mean = sum(data) / len(data)
                col_l, col_r = st.columns([2, 3])
                with col_l:
                    sum_str = " + ".join(str(int(x) if x==int(x) else x) for x in data[:5]) + ("+ ..." if len(data) > 5 else "")
                    st.latex(rf"\text{{Mean}} = \frac{{{sum_str}}}{{{len(data)}}} = \frac{{{sum(data)}}}{{{len(data)}}} = {mean:.4f}")
                with col_r:
                    st.write("**STEP 1** – Mean = sum of all values ÷ count of values.")
                
                if show_teacher_notes:
                    with st.expander("📚 Teacher Notes (Mean)"):
                        st.write(
                            "The **mean** (average) is the sum of all values divided by the number of values. "
                            "It represents the 'typical' value but is affected by extreme outliers."
                        )
                
                # STEP 2: Find median
                sorted_data = sorted(data)
                if len(data) % 2 == 1:
                    median = sorted_data[len(data) // 2]
                    col_l, col_r = st.columns([2, 3])
                    with col_l:
                        st.latex(rf"\text{{Sorted data: }} {sorted_data}")
                        st.latex(rf"\text{{Median}} = \text{{middle value}} = {median}")
                    with col_r:
                        st.write("**STEP 2** – Sort data; median is the middle value (odd count).")
                else:
                    median = (sorted_data[len(data) // 2 - 1] + sorted_data[len(data) // 2]) / 2
                    col_l, col_r = st.columns([2, 3])
                    with col_l:
                        st.latex(rf"\text{{Sorted data: }} {sorted_data}")
                        val1 = sorted_data[len(data)//2-1]
                        val2 = sorted_data[len(data)//2]
                        st.latex(rf"\text{{Median}} = \frac{{{val1} + {val2}}}{{2}} = {median}")
                    with col_r:
                        st.write("**STEP 3** – Middle two values averaged (even count).")
                
                if show_teacher_notes:
                    with st.expander("📚 Teacher Notes (Median)"):
                        st.write(
                            "The **median** is the value that splits the data in half. "
                            "Half the values are below it, half above. Median is resistant to outliers."
                        )
                
                # STEP 3: Find mode
                from collections import Counter
                counts = Counter(data)
                mode_val = counts.most_common(1)[0][0]
                mode_count = counts.most_common(1)[0][1]
                
                col_l, col_r = st.columns([2, 3])
                with col_l:
                    st.latex(rf"\text{{Mode}} = {mode_val} \text{{ (appears }} {mode_count} \text{{ times)}}")
                with col_r:
                    st.write("**STEP 4** – Mode is the value that appears most frequently.")
                
                if show_teacher_notes:
                    with st.expander("📚 Teacher Notes (Mode)"):
                        st.write(
                            "The **mode** is the most frequently occurring value. "
                            "A data set can have multiple modes or no mode (all values appear equally)."
                        )
                
                st.markdown("---")
                st.subheader("Summary Statistics")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Mean (Average)", f"{mean:.2f}")
                with col2:
                    st.metric("Median (Middle)", f"{median:.2f}")
                with col3:
                    st.metric("Mode (Most Frequent)", f"{int(mode_val) if mode_val==int(mode_val) else mode_val}")
        except ValueError:
            st.error("Could not parse data. Use numbers separated by commas.")
    
    if show_quizzes:
        with st.expander("📝 Quiz: Statistics"):
            st.write("**Question 1 (1 mark):** Find the mean of: 2, 4, 6, 8")
            ans1 = st.text_input("Your answer", key="quiz_stat_1")
            if st.button("Check Q1", key="check_stat_1"):
                if ans1.strip() == "5":
                    st.success("✓ Correct! (2+4+6+8)÷4 = 20÷4 = 5. **[1 mark]**")
                else:
                    st.error(f"Expected: 5. Your answer: {ans1}")
            
            st.write("**Question 2 (2 marks):** Find the median of: 3, 1, 4, 1, 5, 9, 2, 6")
            ans2 = st.text_input("Your answer", key="quiz_stat_2")
            if st.button("Check Q2", key="check_stat_2"):
                # Sorted: 1, 1, 2, 3, 4, 5, 6, 9; median = (3+4)/2 = 3.5
                if ans2.strip() in ["3.5", "3,5"]:
                    st.success("✓ Correct! Sorted: 1,1,2,3,4,5,6,9; median = (3+4)÷2 = 3.5. **[2 marks]**")
                else:
                    st.error("Expected: 3.5. Your answer: " + ans2)

