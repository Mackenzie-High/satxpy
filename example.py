#
# Copyright (c) 2024 Mackenzie High. All rights reserved.
#

from pysat.solvers import Glucose3
from satxpy import BooleanExpression, And, Or, Xor, assign

# Create an instance of the Glucose SAT solver.
solver = Glucose3()

# Create a boolean expression that will be solved by the solver.
expr = BooleanExpression(solver)

def full_adder (x, y, carry_in):
    '''
    Boolean expressions for a 1-bit Full Adder circuit.
    '''
    sum_out = Xor(Xor(x, y), carry_in)
    carry_out = Or(And(Xor(x, y), carry_in), And(x, y))
    return sum_out, carry_out

def ripple_carry_adder_4bit (x0, x1, x2, x3, y0, y1, y2, y3):
    '''
    Boolean expressions for a 4-bit Ripple Carry Adder circuit.
    '''
    carry_0 = expr.add_var()
    assign(carry_0, False)
    sum_0, carry_1 = full_adder(x0, y0, carry_0)
    sum_1, carry_2 = full_adder(x1, y1, carry_1)
    sum_2, carry_3 = full_adder(x2, y2, carry_2)
    sum_3, carry_4 = full_adder(x3, y3, carry_3)
    return sum_0, sum_1, sum_2, sum_3, carry_4

# Create four boolean variables.
# Entangle them to represent the number five (0011).
A0 = expr["A0"]
A1 = expr["A1"]
A2 = expr["A2"]
A3 = expr["A3"]
assign(A0, True)
assign(A1, True)
assign(A2, False)
assign(A3, False)

# Create four boolean variables.
# Entangle them to represent the number eight (1000).
B0 = expr["B0"]
B1 = expr["B1"]
B2 = expr["B2"]
B3 = expr["B3"]
assign(B0, False)
assign(B1, False)
assign(B2, False)
assign(B3, True)

# Construct a Ripple Carry Adder circuit over the two binary numbers.
S0, S1, S2, S3, carry = ripple_carry_adder_4bit(A3, A2, A1, A0, B3, B2, B1, B0)

# Solve the expression and print the model.
satisfiable = expr.solve()
print(f"SAT = {satisfiable}") # True
print()

model = expr.get_model()
for variable_name, variable_value in model:
    print(f"{variable_name} was assigned ({variable_value}) by the SAT solver.")
print()

# For fun, let's construct the resulting number!
number = (model[S3.index][1] * 8) + (model[S2.index][1] * 4) + (model[S1.index][1] * 2) + (model[S0.index][1] * 1)
print(f"SUM = {number}")

#
# Copyright (c) 2024 Mackenzie High. All rights reserved.
#
