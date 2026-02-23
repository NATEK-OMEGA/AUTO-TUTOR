# Quadratic Sequence Tutor

A comprehensive Streamlit web app for teaching and learning quadratic sequences using the CAPS Grade 11 curriculum methodology.

## Features

### 1. **Student Mode**
- Input any quadratic sequence (minimum 3 terms)
- Step-by-step solution with classroom explanations
- Left: Algebraic calculations with superscripts
- Right: Plain-language CAPS-aligned explanations
- Real-world verification and term generation
- Interactive examples with practice sequences

### 2. **Teacher Mode** (with notes & quizzes)
- **Detailed Pedagogy:** Teacher notes for each calculation step
  - Why second difference = 2a?
  - How elimination method works?
  - Why verification matters?
- **Interactive Quizzes:** Mark-allocated questions (9.5 total marks)
  - Students try before revealing answers
  - Self-marking approach
  - Step-by-step learning progression

### 3. **Mathematical Etiquette**
- **Result Display:** Clean polynomial formatting
  - Omits coefficient 1: `n²` instead of `1n²`
  - Omits coefficient -1: `-n` instead of `-1n`
  - Drops zero terms: `n² + 3` not `n² + 0n + 3`
- **Calculation Steps:** Full values shown for transparency
  - Students see every working step
  - No hidden arithmetic

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

The app opens in your browser at `http://localhost:8501`

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
- (No other dependencies)

## Author Notes

Created for Grade 11 Mathematics (CAPS Curriculum)
Optimised for classroom and self-study use
