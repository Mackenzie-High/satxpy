# Satxpy

The [satxpy](src/satxpy.py) module trivializes working with boolean expressions and SAT solvers.

## Example

In order to demonstrate ease of expressiveness, this example constructs
a 4-bit [Ripple Carry Adder](https://en.wikipedia.org/wiki/Adder_(electronics)#Ripple-carry_adder)
circuit that adds two binary numbers and produces a binary result.

**Code:**

```python
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
```

**Output:**

```plain
mackenzie@caprica: python3.10 example.py
SAT = True

A0 was assigned (True) by the SAT solver.
A1 was assigned (True) by the SAT solver.
A2 was assigned (False) by the SAT solver.
A3 was assigned (False) by the SAT solver.
B0 was assigned (False) by the SAT solver.
B1 was assigned (False) by the SAT solver.
B2 was assigned (False) by the SAT solver.
B3 was assigned (True) by the SAT solver.
$9 was assigned (False) by the SAT solver.
$10 was assigned (True) by the SAT solver.
$11 was assigned (True) by the SAT solver.
$12 was assigned (True) by the SAT solver.
$13 was assigned (False) by the SAT solver.
$14 was assigned (False) by the SAT solver.
$15 was assigned (False) by the SAT solver.
$16 was assigned (False) by the SAT solver.
$17 was assigned (False) by the SAT solver.
$18 was assigned (False) by the SAT solver.
$19 was assigned (False) by the SAT solver.
$20 was assigned (False) by the SAT solver.
$21 was assigned (False) by the SAT solver.
$22 was assigned (True) by the SAT solver.
$23 was assigned (True) by the SAT solver.
$24 was assigned (True) by the SAT solver.
$25 was assigned (False) by the SAT solver.
$26 was assigned (False) by the SAT solver.
$27 was assigned (False) by the SAT solver.
$28 was assigned (True) by the SAT solver.
$29 was assigned (True) by the SAT solver.
$30 was assigned (True) by the SAT solver.
$31 was assigned (False) by the SAT solver.
$32 was assigned (False) by the SAT solver.
$33 was assigned (False) by the SAT solver.

SUM = 13
mackenzie@caprica:
```

## API

**Named Boolean Functions of Arity 1:**
+ `UNSAT(x)`
+ `FALSE(x)`
+ `TRUE(x)`
+ `VARIES(x)`

The `assign(x, value)` function can be used to apply either `TRUE(x)` or `FALSE(x)` based on the boolean `value`.

**Named Boolean Functions of Arity 2:**
+ `AND(x, y)`
+ `CONVERSE(x, y)`
+ `IFF(x, y)`
+ `IMPLIES_NOT(x, y)`
+ `IMPLIES(x, y)`
+ `NAND(x, y)`
+ `NIMPLY(x, y)`
+ `NOR(x, y)`
+ `OR(x, y)`
+ `XNOR(x, y)`
+ `XOR(x, y)`

**Named Boolean Functions of Arity 3:**
+ `z = And(x, y)`
+ `z = Converse(x, y)`
+ `z = Iff(x, y)`
+ `z = ImpliesNot(x, y)`
+ `z = Implies(x, y)`
+ `z = Nand(x, y)`
+ `z = Nimply(x, y)`
+ `z = Nor(x, y)`
+ `z = Not(x, y)`
+ `z = Or(x, y)`
+ `z = Xnor(x, y)`
+ `z = Xor(x, y)`

The output variable, `z`, can either be passed either implicitly or explicitly, for example:
+ **Option 1, Implicit:** `z = And(x, y)`
+ **Option 2, Explicit:** `And(x, y, z)`

**Unnamed Boolean Functions:**

Any unary, binary, or trinary boolean function can be generated using the `F` function, for example:
+ `Fn(1, x)` generates [BooleanFunction[1, 1]](https://www.wolframalpha.com/input?i=BooleanFunction%5B1%2C+1%5D) over the variable `x`.
+ `Fn(13, x, y)` generates [BooleanFunction[13, 2]](https://www.wolframalpha.com/input?i=BooleanFunction%5B13%2C+2%5D) over the variables `x` and `y`.
+ `Fn(17, x, y, z)` generates [BooleanFunction[17, 3]](https://www.wolframalpha.com/input?i=BooleanFunction%5B17%2C+3%5D) over the variables `x`, `y` and `z`.

**Overloaded Operators:**

The `Var` class overloads the following operator:
+ `~`; therefore, `y = ~x` is equivalent to `y = Not(x)`.
+ `&`; therefore, `z = x & y` is equivalent to `z = And(x, y)`;
+ `|`; therefore, `z = x | y` is equivalent to `z = Or(x, y)`;
+ `^`; therefore, `z = x ^ y` is equivalent to `z = Xor(x, y)`;

## Unit Tests

100% code coverage is maintained by this project's unit tests.

**To Run Unit Tests and Generate Code Coverage Report:**
```bash
coverage run -m unittest discover test
coverage html
google-chrome htmlcov/index.html
```
