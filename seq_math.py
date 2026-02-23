# A math tutoring program to calculate mathematic sequences/patterns with a 
# constant second difference for high scholars using user/learner input values for the sequence 
# (input sequence >= 4 terms) using high school math formula for the quadratic sequence

sequence = []
user_sequence = [input(int("Enter the terms of the sequence(min 4 terms): "))]
terms = sequence.append(user_sequence)

d1 = [sequence[1] - sequence[0], sequence[2] - sequence[1], sequence[3] - sequence[2]]
d2 = [d1[1] - d1[0], d1[2] - d1[1]]

general_term = 'Tn = an^2 + bn + c'

def term_one(general_term):
    # substitute the first term into the general term formula --> Equation #1 using the first term of the sequence
    equation_1 = general_term.replace('Tn', sequence[0]) 
    equation_1 = general_term[2:].replace('n', 1) # replace 'n' after the equal sign with the position of the chosen term to use to find the general formula. If Tn = 5, the remaining 'n' after the equal sign will be the first position [0]
    # Return the outcome after substitution
    return equation_1

def term_two(general_term):
    # substitute the first term into the general term formula --> Equation #1 using the first term of the sequence
    equation_2 = general_term.replace('Tn', sequence[1]) 
    equation_2 = general_term[2:].replace('n', 2) # replace 'n' after the equal sign with the position of the chosen term to use to find the general formula. If Tn = 5, the remaining 'n' after the equal sign will be the first position [0]
    # Return the outcome after substitution
    return equation_2

def equation_3(equation_1, equation_2):
    # This is where equation #2 values are subtracted from equation #1 values
    equation_3 = f"{equation_1[0] - equation_2[0]}" + '=' + f"{equation_1[2] - equation_1[2]}" + "+" + f"{equation_1[3] - equation_1[3]}" + "+" + f"{equation_1[4] - equation_1[4]}"
    return equation_3

