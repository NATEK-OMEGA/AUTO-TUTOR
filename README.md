# AUTO‑Tutor: CAPS Mathematics

A Streamlit web app covering the full Grade 10–12 South African CAPS mathematics curriculum.  
Originally built as a quadratic sequence tutor, the application has been extended into a general-purpose maths learning tool. Users select a grade and topic, then work through interactive examples and step-by-step explanations.

## Features

### 1. **Student Mode**
- Choose a grade (10, 11 or 12) and a topic from the CAPS curriculum
- Enter values or expressions as prompted by the topic module
- View step-by-step solutions, calculations, interactive charts and diagrams
- Quizzes with self‑marking and optional teacher commentary help assess comprehension
- Modular design makes it easy to extend and refactor topics

### 2. **Teacher Mode** (with notes & quizzes)
- Enable expanded pedagogy across all topics
  - Mathematics reasoning linked to CAPS outcomes
  - Optional hints, teacher commentary and worked examples
- **Interactive Quizzes:** built into each topic where appropriate
  - Questions are mark‑allocated and self‑assessed
  - Teachers can toggle visibility of answers for formative assessment

### 3. **Mathematical Etiquette**
- Clean formatting and explanation tailored to each topic
- Calculations are fully shown with intermediate steps, supporting CAPS expectations for rigour

### 4. **CAPS Alignment**
- Follows the Grade 11 CAPS curriculum method:
  1. Calculate first differences
  2. Calculate second differences
  3. Verify constant second difference
  4. Use 2a property to find coefficient a
  5. Form and solve systems of linear equations
  6. Verify formula with original sequence

## Installation

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
streamlit run seq_math_app.py
```

The app opens in your browser at `http://localhost:8501`.  
Select a grade and topic from the drop‑down menus, then follow the on‑screen instructions for that topic.

### Student Workflow
1. Select **"Student (solve)"** mode
2. Enter your sequence (e.g., `2, 7, 14, 23`)
3. Toggle "Show detailed steps" for explanations
4. Click "Compute general term"
5. Use the **Explore** section to find T(n) for any n

### Teacher Workflow
1. Select **"Teacher (with notes & quizzes)"** mode
2. Enter your sequence or load an example
3. Students see:
   - Each step with classroom explanation
   - **📚 Teacher Notes** expandable sections
   - **Interactive Quiz** sections with mark allocations
4. Total quiz marks: **9.5** across all steps

## Examples Built In

- **Squares:** 1, 4, 9, 16 → T(n) = n²
- **Starts at 3:** 3, 8, 15, 24 → T(n) = n² + 2n
- **Shifted:** 2, 7, 14, 23 → T(n) = n² + 2n - 1

## Mark Allocations (Teacher Mode)

- Step 1: First differences — 2 marks
- Step 2: Second differences — 2 marks
- Step 3: Constant property — 1.5 marks
- Step 4: Finding a — 1.5 marks
- Step 5: Forming equations — 2 marks
- Steps 6–7: Finding b & c — 0.5 marks each
- **Total: 9.5 marks**

## Pedagogical Notes

This app embeds several CAPS principles:

1. **Concrete → Abstract:** Starts with numerical patterns, leads to algebraic formulas
2. **Problem-Solving:** Students use sequence analysis to discover polynomial structure
3. **Verification Culture:** Always check answers by substituting back
4. **Algebraic Thinking:** Elimination method for solving systems of equations
5. **Communication:** Explain reasoning at each step (builds mathematical language)

## Files

- `seq_math_app.py` — Main Streamlit application
- `requirements.txt` — Python dependencies
- `README.md` — This file

## Requirements

- Python 3.8+
- Streamlit
- NumPy and Matplotlib (for charts/graphics)

## Author Notes

Created as an educational tool for South African CAPS Mathematics (Grades 10–12).  
Optimised for classroom and self-study use.


## Version 2.1 update

This release transforms the original Grade 11 quadratic sequence tutor into a
full‑fledged CAPS mathematics learning platform. Key changes include:

- **Modular architecture:** topic handlers moved into `topics/` package with
  separate modules for grade‑10, grade‑11, grade‑12 and shared quadratic logic.
- **Grade/topic selectors:** users now pick Grade 10, 11 or 12 and then a topic
  from the curriculum list rather than only quadratic sequences.
- **Expanded topics:** dozens of new interactive modules added across grades,
  including algebra, finance, measurement, trigonometry, probability,
  linear/exponential functions, calculus, analytic and Euclidean geometry.
- **Teacher notes & quizzes:** every topic contains pedagogy expanders and
  built‑in self‑marking quiz questions with mark allocations.
- **Graphics:** Matplotlib charts support unit circle diagrams, linear plots,
  angle supplements, circle equations, etc. Dependencies added (`numpy`,
  `matplotlib`).
- **Refactor & cleanup:** original quadratic code relocated to its own module;
  page wrappers simplified; home page rewritten; README enhanced with new
  usage instructions.
- **Type safety & testing:** Pylance errors cleared, type hints improved,
  example import tests added to verify handler registrations.

This update lays the groundwork for further curriculum coverage and makes the
codebase easier to maintain and extend.

## Version 2.2 Update: Step-by-Step Pedagogical Explanations

This release enhances all 18+ topic handlers across Grades 10–12 with **comprehensive step-by-step calculations and explanations**, mirroring the detailed pedagogical approach used in the original quadratic sequence tutor.

### Enhancements by Grade

#### Grade 10 (6 handlers)
- **Numbers & Patterns**: First-differences calculation step-by-step with each subtraction labelled
- **Algebra: Expressions & Equations**: Balance method broken into STEP 1 (subtract), STEP 2 (divide), STEP 3 (verify)
- **Finance Mathematics**: Simple & Compound Interest split into 5-step workflows with formula display
- **Measurement & Geometry**: Area/perimeter formulas with step-by-step application (rectangles, circles, triangles)
- **Trigonometry**: SOH-CAH-TOA ratios with unit circle diagrams; STEP 1–3 walkthrough
- **Probability & Statistics**: Mean/median/mode with sorted data and intermediate steps

#### Grade 11 (5 handlers)
- **Linear Functions**: Gradient-intercept breakdown; x/y-intercept calculation; graphing
- **Quadratic Sequences**: Delegates to comprehensive quadratic module (500+ lines of pedagogy)
- **Exponential Functions**: Exponential vs linear growth comparison; graph plotting
- **Euclidean Geometry**: Supplementary/alternate angles; inscribed angle theorem with diagrams

#### Grade 12 (6 handlers)
- **Calculus: Differentiation**: Power rule applied step-by-step; slope at specific points
- **Calculus: Integration**: Reverse process with each term; constant of integration explained
- **Trigonometric Identities**: Pythagorean identity (sin²θ + cos²θ = 1); double angle formula
- **Analytic Geometry**: Circle equation derivation; standard form; point-on-circle tests

### Pedagogical Workflow

Each handler follows: STEP 0 (setup) → STEP 1–3 (calculations) → Verification → 📚 Teacher Notes → 📝 Quizzes

### Technical Improvements

- Two-column layout: LaTeX on left, explanation on right
- Graphics: Matplotlib unit circles, angle diagrams, function graphs
- All imports: NumPy and Matplotlib added to topic modules
- Code reuse: Statistics/Finance delegated in Grade 12
- Validation: All modules pass Pylance (0 errors)

