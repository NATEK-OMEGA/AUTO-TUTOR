import streamlit as st
from typing import List, Tuple, Dict, Any

# --- quadratic sequence logic reused across grades ---

def compute_quadratic_from_terms(seq: List[float]) -> Tuple[float, float, float, Dict[str, Any]]:
    if len(seq) < 3:
        raise ValueError("Need at least 3 terms to determine a quadratic")
    d1 = [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]
    d2 = [d1[i + 1] - d1[i] for i in range(len(d1) - 1)]
    details: Dict[str, Any] = {"sequence": seq, "d1": d1, "d2": d2, "explanations": [], "step_texts": {},}
    # explanations omitted for brevity (copy from original implementation)
    # ... we will copy the full original content exactly so the module behaves identically.
    # For brevity I will include the full function as in seq_math_app earlier.

    # Add classroom-style explanation about differences
    details["step_texts"]["what_differences"] = (
        "First differences are found by subtracting each term from the next: "
        "they show how the sequence changes from term to term. Second differences "
        "are differences of those first differences. For quadratic sequences the second "
        "differences are constant."
    )
    details["step_texts"]["teacher_note_differences"] = (
        "This difference method is the foundation of sequence analysis in CAPS. It's visual, intuitive, and builds "
        "problem-solving skills. Students should practise: it trains algebraic thinking and pattern recognition."
    )
    tol = 1e-9
    if not all(abs(d2[i] - d2[0]) <= tol for i in range(len(d2))):
        details["explanations"].append("Second differences are not constant; sequence is not quadratic.")
        details["step_texts"]["why_not_quadratic"] = (
            "Because the second differences are not the same the sequence cannot be exactly "
            "represented by a quadratic polynomial of the form T(n)=an^2+bn+c."
        )
        raise ValueError("Sequence does not have constant second difference (not quadratic)")
    second_diff = d2[0]
    a = second_diff / 2.0
    details["explanations"].append(f"Second difference = {second_diff} → a = second_diff/2 = {a}")
    details["step_texts"]["compute_a"] = (
        "The second difference for a quadratic sequence equals 2a. So divide the constant "
        "second difference by 2 to find a."
    )
    details["step_texts"]["teacher_note_a"] = (
        "Why does the second difference equal 2a? For a quadratic T(n)=an²+bn+c, the first differences form "
        "a linear sequence with slope 2a. The constant difference between these linear first differences is always 2a. "
        "This is a key property used in CAPS curriculum to identify and solve quadratic sequences."
    )
    T1 = seq[0]
    T2 = seq[1]
    dT = T2 - T1
    b = dT - 3 * a
    c = T1 - a - b
    details["explanations"].append(f"T1 = {T1}, T2 = {T2}; T2 - T1 = {dT}")
    details["step_texts"]["explain_T1_T2"] = (
        "We substitute n=1 and n=2 into T(n)=an^2+bn+c to form two equations:",
    )
    details["step_texts"]["teacher_note_equations"] = (
        "The general term T(n)=an²+bn+c is a polynomial with three unknowns. We need three independent equations "
        "to solve for a, b, and c uniquely. We already have 'a' from the second difference, so we form two equations "
        "from the first and second terms. This system of linear equations can be solved by elimination—a fundamental "
        "algebraic technique taught in Grade 10-11 CAPS algebra."
    )
    details["step_texts"]["compute_b"] = (
        "Subtract the two equations to eliminate c: (4a+2b+c) - (a+b+c) = 3a + b. "
        "So b = (T2 - T1) - 3a."
    )
    details["step_texts"]["teacher_note_b"] = (
        "Elimination is a powerful strategy: by subtracting equation (1) from equation (2), the constant term 'c' "
        "cancels out. This is intentional—we design our equations to eliminate unknowns strategically. "
        "Students should practise this technique: identify which equations to use and which variable to eliminate."
    )
    details["step_texts"]["compute_c"] = (
        "Finally, substitute a and b back into a + b + c = T1 to solve for c."
    )
    details["step_texts"]["teacher_note_c"] = (
        "Back-substitution completes the solution. Once we know a and b, we can substitute them into any of our "
        "original equations to find c. This is the third step of the elimination method. Emphasise that the choice "
        "of which equation to use doesn't matter—they're equivalent; all should give the same answer (a good verification check)."
    )
    details["explanations"].append(f"3a + b = T2 - T1 → b = {dT} - 3×{a} = {b}")
    details["explanations"].append(f"c = T1 - a - b = {T1} - {a} - {b} = {c}")
    generated = [a * (n ** 2) + b * n + c for n in range(1, len(seq) + 1)]
    details["generated"] = generated
    details["explanations"].append("Verification: Generated terms using computed a,b,c should match input sequence.")
    details["step_texts"]["verification"] = (
        "To verify, we generate terms from the formula T(n)=an^2+bn+c for the same n values. "
        "If the generated terms match the input sequence the formula is correct."
    )
    details["step_texts"]["teacher_note_verification"] = (
        "Verification is not optional—it's essential mathematical practice. Always substitute back into the original "
        "problem to check your answer. In this case, our formula should reproduce the input sequence exactly. "
        "If it doesn't, we've made an error somewhere in our calculations (or the sequence isn't quadratic). "
        "This builds problem-solving habits and mathematical rigour."
    )
    return a, b, c, details


def format_num_for_display(x: float) -> str:
    if abs(x - round(x)) < 1e-9:
        return str(int(round(x)))
    s = f"{x:.8f}".rstrip('0').rstrip('.')
    return s


def latex_polynomial_elegant(a: float, b: float, c: float) -> str:
    tol = 1e-9
    parts = []
    if abs(a) > tol:
        a_disp = format_num_for_display(a)
        if abs(abs(a) - 1.0) < tol:
            if a > 0:
                parts.append("n^{2}")
            else:
                parts.append("- n^{2}")
        else:
            if a > 0 and parts:
                parts.append(f"+ {a_disp}n^{{2}}")
            elif a < 0:
                parts.append(f"- {format_num_for_display(abs(a))}n^{{2}}")
            else:
                parts.append(f"{a_disp}n^{{2}}")
    if abs(b) > tol:
        b_disp = format_num_for_display(abs(b))
        if abs(abs(b) - 1.0) < tol:
            if b > 0:
                if parts:
                    parts.append("+ n")
                else:
                    parts.append("n")
            else:
                parts.append("- n")
        else:
            if b > 0:
                if parts:
                    parts.append(f"+ {b_disp}n")
                else:
                    parts.append(f"{b_disp}n")
            else:
                parts.append(f"- {b_disp}n")
    if abs(c) > tol:
        c_disp = format_num_for_display(abs(c))
        if c > 0:
            if parts:
                parts.append(f"+ {c_disp}")
            else:
                parts.append(f"{c_disp}")
        else:
            parts.append(f"- {c_disp}")
    if not parts:
        return "0"
    return " ".join(parts)


def display_steps(details: Dict[str, Any], a: float, b: float, c: float,
                  show_teacher_notes: bool = False, show_quizzes: bool = False) -> None:
    # same implementation as before, but copy entire function body
    seq_str = ", ".join(format_num_for_display(x) for x in details["sequence"])
    col_l, col_r = st.columns([2, 3])
    with col_l:
        st.latex(r"\textbf{Given\ sequence:}\ %s" % seq_str)
    with col_r:
        st.write("STEP 0 — What we are given: the first terms of the sequence.")
    if show_teacher_notes and "teacher_note_differences" in details.get("step_texts", {}):
        with st.expander("📚 Teacher Notes (Step 0)"):
            st.write(details["step_texts"].get("teacher_note_differences", ""))
    d1_str = ", ".join(format_num_for_display(x) for x in details["d1"])
    col_l, col_r = st.columns([2, 3])
    with col_l:
        st.latex(r"\textbf{First\ differences:}\ %s" % d1_str)
    with col_r:
        st.write("STEP 1 — Find first differences: subtract each term from the next to see how the sequence changes.")
    if show_teacher_notes:
        with st.expander("📚 Teacher Notes (Step 1)"):
            st.write("**First differences:** represent the rate of change. For a quadratic sequence, first differences form a linear sequence. "
                    "This is a key insight: quadratic → linear first differences → constant second differences.")
    if show_quizzes:
        st.info("**Interactive Quiz for Step 1** — 2 marks")
        if st.button("Try the Step 1 quiz", key="quiz_step1"):
            st.write("Calculate first differences for the given sequence.")
            student_answer = st.text_input("Enter first differences (comma-separated):", key="ans_step1")
            if st.button("Check", key="check_step1"):
                st.info(f"Expected: {d1_str}")
        st.divider()
    d2_str = ", ".join(format_num_for_display(x) for x in details["d2"])
    col_l, col_r = st.columns([2, 3])
    with col_l:
        st.latex(r"\textbf{Second\ differences:}\ %s" % d2_str)
    with col_r:
        st.write(details.get("step_texts", {}).get("what_differences", ""))
    if show_teacher_notes:
        with st.expander("📚 Teacher Notes (Step 2)"):
            st.write("**Second differences:** If these are constant, the sequence is quadratic. This is the CAPS-endorsed method for "
                    "identifying quadratic sequences at Grade 11. Constant second difference is the hallmark of quadratic behaviour.")
    second_diff = details["d2"][0]
    col_l, col_r = st.columns([2, 3])
    with col_l:
        st.latex(r"\text{Second difference} = %s \Rightarrow a = \frac{%s}{2} = %s" % (
            format_num_for_display(second_diff), format_num_for_display(second_diff), format_num_for_display(a)
        ))
    with col_r:
        st.write("STEP 3 — Determine 'a': For quadratic sequences the second difference equals 2a, so divide by 2 to find a.")
    if show_teacher_notes:
        with st.expander("📚 Teacher Notes (Step 3)"):
            st.write(details.get("step_texts", {}).get("teacher_note_a", ""))
    T1 = details["sequence"][0]
    T2 = details["sequence"][1]
    col_l, col_r = st.columns([2, 3])
    with col_l:
        st.latex((r"a + b + c = %s" % format_num_for_display(T1)) + " ...equation (1)")
        st.latex((r"4a + 2b + c = %s" % format_num_for_display(T2)) + " ...equation (2)")
    with col_r:
        st.write("STEP 4 — Form two equations by substituting n=1 and n=2 into T(n)=an^2+bn+c.")
    if show_teacher_notes:
        with st.expander("📚 Teacher Notes (Step 4)"):
            st.write(details.get("step_texts", {}).get("teacher_note_equations", ""))
    col_l, col_r = st.columns([2, 3])
    with col_l:
        st.latex(r"(4a+2b+c) - (a+b+c) = 3a + b = %s" % format_num_for_display(T2 - T1))
        st.latex(r"b = %s - 3\times %s = %s" % (format_num_for_display(T2 - T1), format_num_for_display(a), format_num_for_display(b)))
    with col_r:
        st.write(details.get("step_texts", {}).get("compute_b", ""))
    if show_teacher_notes:
        with st.expander("📚 Teacher Notes (Step 5 — Finding b)"):
            st.write(details.get("step_texts", {}).get("teacher_note_b", ""))
    col_l, col_r = st.columns([2, 3])
    with col_l:
        st.latex(r"c = %s - %s - %s = %s" % (format_num_for_display(T1), format_num_for_display(a), format_num_for_display(b), format_num_for_display(c)))
    with col_r:
        st.write(details.get("step_texts", {}).get("compute_c", ""))
    if show_teacher_notes:
        with st.expander("📚 Teacher Notes (Step 6 — Finding c)"):
            st.write(details.get("step_texts", {}).get("teacher_note_c", ""))
    col_l, col_r = st.columns([2, 3])
    with col_l:
        st.latex(r"\text{Verification (generated terms)}: %s" % (", ".join(format_num_for_display(x) for x in details.get("generated", []))))
    with col_r:
        st.write(details.get("step_texts", {}).get("verification", ""))
    if show_teacher_notes:
        with st.expander("📚 Teacher Notes (Step 7 — Verification)"):
            st.write(details.get("step_texts", {}).get("teacher_note_verification", ""))


def quadratic_sequence_module(show_teacher_notes: bool, show_quizzes: bool):
    st.subheader("Quadratic Sequences and General Term")
    st.write(
        "Enter the first terms of a quadratic sequence (at least 3 terms). The app will "
        "find the general term $T(n)=an^2+bn+c$ and walk through CAPS-aligned reasoning."
    )
    seq_input = st.text_input("Sequence terms (comma-separated, e.g. 3, 8, 15, 24)", value="1,4,9,16")
    show_steps = st.checkbox("Show detailed steps", value=True)
    compute_button = st.button("Compute general term")

    def compute_and_display_from_list(seq: List[float]):
        try:
            a, b, c, details = compute_quadratic_from_terms(seq)
        except ValueError as e:
            st.error(f"Error: {e}")
            return

        if show_steps:
            st.subheader("Step-by-step explanation")
            display_steps(details, a, b, c, show_teacher_notes=show_teacher_notes, show_quizzes=show_quizzes)

        st.subheader("Result")
        st.latex(r"T(n) = %s" % latex_polynomial_elegant(a, b, c))
        st.write(f"Computed coefficients: a = {format_num_for_display(a)}, b = {format_num_for_display(b)}, c = {format_num_for_display(c)}")

        # allow user to compute further terms or specific nth term
        st.subheader("Explore")
        n = st.number_input("Compute T(n) for n =", min_value=1, value=len(seq) + 1, step=1)
        Tn = a * (n ** 2) + b * n + c
        st.write(f"T({n}) = {format_num_for_display(Tn)}")

        count = st.number_input("Generate next how many terms?", min_value=0, value=3, step=1)
        if count > 0:
            start = len(seq) + 1
            more = [a * (i ** 2) + b * i + c for i in range(start, start + count)]
            st.write("Next terms:", [format_num_for_display(x) for x in more])

    if compute_button:
        try:
            seq = [float(x.strip()) for x in seq_input.split(",") if x.strip() != ""]
            if len(seq) < 3:
                st.error("Please enter at least 3 terms.")
            else:
                compute_and_display_from_list(seq)
        except ValueError as e:
            st.error(f"Error parsing input: {e}")

    with st.expander("Examples & Practice"):
        st.write("Choose an example sequence to load a worked example:")
        examples = {
            "Squares (1,4,9,16)": [1, 4, 9, 16],
            "Starts at 3 (3,8,15,24)": [3, 8, 15, 24],
            "Shifted (2,7,14,23)": [2, 7, 14, 23],
        }
        choice = st.selectbox("Select example:", list(examples.keys()))
        if st.button("Load example"):
            ex_seq = examples[choice]
            seq_input = ",".join(format_num_for_display(x) for x in ex_seq)
            st.write("Loaded sequence:", seq_input)
            compute_and_display_from_list([float(x) for x in ex_seq])
