#
# Copyright (c) 2024 Mackenzie High. All rights reserved.
#

# These are all of the boolean functions of arity one, two, and three.
# These are the CNF representations of those functions in minimal form.
# The minimal forms where computed using the Quine-McCluskey algorithm in SymPy.
# See: https://docs.sympy.org/latest/modules/logic.html
CLAUSES = dict()
CLAUSES[(1, 0)] = [[1], [-1]]
CLAUSES[(1, 1)] = [[-1]]
CLAUSES[(1, 2)] = [[1]]
CLAUSES[(1, 3)] = [[1, -1]]
CLAUSES[(2, 0)] = [[1], [-1]]
CLAUSES[(2, 1)] = [[-1], [-2]]
CLAUSES[(2, 2)] = [[2], [-1]]
CLAUSES[(2, 3)] = [[-1]]
CLAUSES[(2, 4)] = [[1], [-2]]
CLAUSES[(2, 5)] = [[-2]]
CLAUSES[(2, 6)] = [[1, 2], [-1, -2]]
CLAUSES[(2, 7)] = [[-1, -2]]
CLAUSES[(2, 8)] = [[1], [2]]
CLAUSES[(2, 9)] = [[1, -2], [2, -1]]
CLAUSES[(2, 10)] = [[2]]
CLAUSES[(2, 11)] = [[2, -1]]
CLAUSES[(2, 12)] = [[1]]
CLAUSES[(2, 13)] = [[1, -2]]
CLAUSES[(2, 14)] = [[1, 2]]
CLAUSES[(2, 15)] = []
CLAUSES[(3, 0)] = [[1], [-1]]
CLAUSES[(3, 1)] = [[-1], [-2], [-3]]
CLAUSES[(3, 2)] = [[3], [-1], [-2]]
CLAUSES[(3, 3)] = [[-1], [-2]]
CLAUSES[(3, 4)] = [[2], [-1], [-3]]
CLAUSES[(3, 5)] = [[-1], [-3]]
CLAUSES[(3, 6)] = [[-1], [2, 3], [-2, -3]]
CLAUSES[(3, 7)] = [[-1], [-2, -3]]
CLAUSES[(3, 8)] = [[2], [3], [-1]]
CLAUSES[(3, 9)] = [[-1], [2, -3], [3, -2]]
CLAUSES[(3, 10)] = [[3], [-1]]
CLAUSES[(3, 11)] = [[-1], [3, -2]]
CLAUSES[(3, 12)] = [[2], [-1]]
CLAUSES[(3, 13)] = [[-1], [2, -3]]
CLAUSES[(3, 14)] = [[-1], [2, 3]]
CLAUSES[(3, 15)] = [[-1]]
CLAUSES[(3, 16)] = [[1], [-2], [-3]]
CLAUSES[(3, 17)] = [[-2], [-3]]
CLAUSES[(3, 18)] = [[-2], [1, 3], [-1, -3]]
CLAUSES[(3, 19)] = [[-2], [-1, -3]]
CLAUSES[(3, 20)] = [[-3], [1, 2], [-1, -2]]
CLAUSES[(3, 21)] = [[-3], [-1, -2]]
CLAUSES[(3, 22)] = [[1, 2, 3], [-1, -2], [-1, -3], [-2, -3]]
CLAUSES[(3, 23)] = [[-1, -2], [-1, -3], [-2, -3]]
CLAUSES[(3, 24)] = [[1, 2], [3, -2], [-1, -3]]
CLAUSES[(3, 25)] = [[2, -3], [3, -2], [-1, -3]]
CLAUSES[(3, 26)] = [[1, 3], [3, -2], [-1, -3]]
CLAUSES[(3, 27)] = [[3, -2], [-1, -3]]
CLAUSES[(3, 28)] = [[1, 2], [2, -3], [-1, -2]]
CLAUSES[(3, 29)] = [[2, -3], [-1, -2]]
CLAUSES[(3, 30)] = [[1, 2, 3], [-1, -2], [-1, -3]]
CLAUSES[(3, 31)] = [[-1, -2], [-1, -3]]
CLAUSES[(3, 32)] = [[1], [3], [-2]]
CLAUSES[(3, 33)] = [[-2], [1, -3], [3, -1]]
CLAUSES[(3, 34)] = [[3], [-2]]
CLAUSES[(3, 35)] = [[-2], [3, -1]]
CLAUSES[(3, 36)] = [[1, 2], [3, -1], [-2, -3]]
CLAUSES[(3, 37)] = [[1, -3], [3, -1], [-2, -3]]
CLAUSES[(3, 38)] = [[2, 3], [3, -1], [-2, -3]]
CLAUSES[(3, 39)] = [[3, -1], [-2, -3]]
CLAUSES[(3, 40)] = [[3], [1, 2], [-1, -2]]
CLAUSES[(3, 41)] = [[3, -1], [3, -2], [-1, -2], [1, 2, -3]]
CLAUSES[(3, 42)] = [[3], [-1, -2]]
CLAUSES[(3, 43)] = [[3, -1], [3, -2], [-1, -2]]
CLAUSES[(3, 44)] = [[1, 2], [2, 3], [-1, -2]]
CLAUSES[(3, 45)] = [[3, -1], [-1, -2], [1, 2, -3]]
CLAUSES[(3, 46)] = [[2, 3], [-1, -2]]
CLAUSES[(3, 47)] = [[3, -1], [-1, -2]]
CLAUSES[(3, 48)] = [[1], [-2]]
CLAUSES[(3, 49)] = [[-2], [1, -3]]
CLAUSES[(3, 50)] = [[-2], [1, 3]]
CLAUSES[(3, 51)] = [[-2]]
CLAUSES[(3, 52)] = [[1, 2], [1, -3], [-1, -2]]
CLAUSES[(3, 53)] = [[1, -3], [-1, -2]]
CLAUSES[(3, 54)] = [[1, 2, 3], [-1, -2], [-2, -3]]
CLAUSES[(3, 55)] = [[-1, -2], [-2, -3]]
CLAUSES[(3, 56)] = [[1, 2], [1, 3], [-1, -2]]
CLAUSES[(3, 57)] = [[3, -2], [-1, -2], [1, 2, -3]]
CLAUSES[(3, 58)] = [[1, 3], [-1, -2]]
CLAUSES[(3, 59)] = [[3, -2], [-1, -2]]
CLAUSES[(3, 60)] = [[1, 2], [-1, -2]]
CLAUSES[(3, 61)] = [[-1, -2], [1, 2, -3]]
CLAUSES[(3, 62)] = [[1, 2, 3], [-1, -2]]
CLAUSES[(3, 63)] = [[-1, -2]]
CLAUSES[(3, 64)] = [[1], [2], [-3]]
CLAUSES[(3, 65)] = [[-3], [1, -2], [2, -1]]
CLAUSES[(3, 66)] = [[1, 3], [2, -1], [-2, -3]]
CLAUSES[(3, 67)] = [[1, -2], [2, -1], [-2, -3]]
CLAUSES[(3, 68)] = [[2], [-3]]
CLAUSES[(3, 69)] = [[-3], [2, -1]]
CLAUSES[(3, 70)] = [[2, 3], [2, -1], [-2, -3]]
CLAUSES[(3, 71)] = [[2, -1], [-2, -3]]
CLAUSES[(3, 72)] = [[2], [1, 3], [-1, -3]]
CLAUSES[(3, 73)] = [[2, -1], [2, -3], [-1, -3], [1, 3, -2]]
CLAUSES[(3, 74)] = [[1, 3], [2, 3], [-1, -3]]
CLAUSES[(3, 75)] = [[2, -1], [-1, -3], [1, 3, -2]]
CLAUSES[(3, 76)] = [[2], [-1, -3]]
CLAUSES[(3, 77)] = [[2, -1], [2, -3], [-1, -3]]
CLAUSES[(3, 78)] = [[2, 3], [-1, -3]]
CLAUSES[(3, 79)] = [[2, -1], [-1, -3]]
CLAUSES[(3, 80)] = [[1], [-3]]
CLAUSES[(3, 81)] = [[-3], [1, -2]]
CLAUSES[(3, 82)] = [[1, 3], [1, -2], [-1, -3]]
CLAUSES[(3, 83)] = [[1, -2], [-1, -3]]
CLAUSES[(3, 84)] = [[-3], [1, 2]]
CLAUSES[(3, 85)] = [[-3]]
CLAUSES[(3, 86)] = [[1, 2, 3], [-1, -3], [-2, -3]]
CLAUSES[(3, 87)] = [[-1, -3], [-2, -3]]
CLAUSES[(3, 88)] = [[1, 2], [1, 3], [-1, -3]]
CLAUSES[(3, 89)] = [[2, -3], [-1, -3], [1, 3, -2]]
CLAUSES[(3, 90)] = [[1, 3], [-1, -3]]
CLAUSES[(3, 91)] = [[-1, -3], [1, 3, -2]]
CLAUSES[(3, 92)] = [[1, 2], [-1, -3]]
CLAUSES[(3, 93)] = [[2, -3], [-1, -3]]
CLAUSES[(3, 94)] = [[1, 2, 3], [-1, -3]]
CLAUSES[(3, 95)] = [[-1, -3]]
CLAUSES[(3, 96)] = [[1], [2, 3], [-2, -3]]
CLAUSES[(3, 97)] = [[1, -2], [1, -3], [-2, -3], [2, 3, -1]]
CLAUSES[(3, 98)] = [[1, 3], [2, 3], [-2, -3]]
CLAUSES[(3, 99)] = [[1, -2], [-2, -3], [2, 3, -1]]
CLAUSES[(3, 100)] = [[1, 2], [2, 3], [-2, -3]]
CLAUSES[(3, 101)] = [[1, -3], [-2, -3], [2, 3, -1]]
CLAUSES[(3, 102)] = [[2, 3], [-2, -3]]
CLAUSES[(3, 103)] = [[-2, -3], [2, 3, -1]]
CLAUSES[(3, 104)] = [[1, 2], [1, 3], [2, 3], [-1, -2, -3]]
CLAUSES[(3, 105)] = [[1, 2, -3], [1, 3, -2], [2, 3, -1], [-1, -2, -3]]
CLAUSES[(3, 106)] = [[1, 3], [2, 3], [-1, -2, -3]]
CLAUSES[(3, 107)] = [[1, 3, -2], [2, 3, -1], [-1, -2, -3]]
CLAUSES[(3, 108)] = [[1, 2], [2, 3], [-1, -2, -3]]
CLAUSES[(3, 109)] = [[1, 2, -3], [2, 3, -1], [-1, -2, -3]]
CLAUSES[(3, 110)] = [[2, 3], [-1, -2, -3]]
CLAUSES[(3, 111)] = [[2, 3, -1], [-1, -2, -3]]
CLAUSES[(3, 112)] = [[1], [-2, -3]]
CLAUSES[(3, 113)] = [[1, -2], [1, -3], [-2, -3]]
CLAUSES[(3, 114)] = [[1, 3], [-2, -3]]
CLAUSES[(3, 115)] = [[1, -2], [-2, -3]]
CLAUSES[(3, 116)] = [[1, 2], [-2, -3]]
CLAUSES[(3, 117)] = [[1, -3], [-2, -3]]
CLAUSES[(3, 118)] = [[1, 2, 3], [-2, -3]]
CLAUSES[(3, 119)] = [[-2, -3]]
CLAUSES[(3, 120)] = [[1, 2], [1, 3], [-1, -2, -3]]
CLAUSES[(3, 121)] = [[1, 2, -3], [1, 3, -2], [-1, -2, -3]]
CLAUSES[(3, 122)] = [[1, 3], [-1, -2, -3]]
CLAUSES[(3, 123)] = [[1, 3, -2], [-1, -2, -3]]
CLAUSES[(3, 124)] = [[1, 2], [-1, -2, -3]]
CLAUSES[(3, 125)] = [[1, 2, -3], [-1, -2, -3]]
CLAUSES[(3, 126)] = [[1, 2, 3], [-1, -2, -3]]
CLAUSES[(3, 127)] = [[-1, -2, -3]]
CLAUSES[(3, 128)] = [[1], [2], [3]]
CLAUSES[(3, 129)] = [[1, -3], [2, -1], [3, -2]]
CLAUSES[(3, 130)] = [[3], [1, -2], [2, -1]]
CLAUSES[(3, 131)] = [[1, -2], [2, -1], [3, -2]]
CLAUSES[(3, 132)] = [[2], [1, -3], [3, -1]]
CLAUSES[(3, 133)] = [[1, -3], [2, -3], [3, -1]]
CLAUSES[(3, 134)] = [[2, 3], [2, -1], [3, -1], [1, -2, -3]]
CLAUSES[(3, 135)] = [[2, -1], [3, -1], [1, -2, -3]]
CLAUSES[(3, 136)] = [[2], [3]]
CLAUSES[(3, 137)] = [[2, -1], [2, -3], [3, -2]]
CLAUSES[(3, 138)] = [[3], [2, -1]]
CLAUSES[(3, 139)] = [[2, -1], [3, -2]]
CLAUSES[(3, 140)] = [[2], [3, -1]]
CLAUSES[(3, 141)] = [[2, -3], [3, -1]]
CLAUSES[(3, 142)] = [[2, 3], [2, -1], [3, -1]]
CLAUSES[(3, 143)] = [[2, -1], [3, -1]]
CLAUSES[(3, 144)] = [[1], [2, -3], [3, -2]]
CLAUSES[(3, 145)] = [[1, -3], [2, -3], [3, -2]]
CLAUSES[(3, 146)] = [[1, 3], [1, -2], [3, -2], [2, -1, -3]]
CLAUSES[(3, 147)] = [[1, -2], [3, -2], [2, -1, -3]]
CLAUSES[(3, 148)] = [[1, 2], [1, -3], [2, -3], [3, -1, -2]]
CLAUSES[(3, 149)] = [[1, -3], [2, -3], [3, -1, -2]]
CLAUSES[(3, 150)] = [[1, 2, 3], [1, -2, -3], [2, -1, -3], [3, -1, -2]]
CLAUSES[(3, 151)] = [[1, -2, -3], [2, -1, -3], [3, -1, -2]]
CLAUSES[(3, 152)] = [[1, 2], [2, -3], [3, -2]]
CLAUSES[(3, 153)] = [[2, -3], [3, -2]]
CLAUSES[(3, 154)] = [[1, 3], [3, -2], [2, -1, -3]]
CLAUSES[(3, 155)] = [[3, -2], [2, -1, -3]]
CLAUSES[(3, 156)] = [[1, 2], [2, -3], [3, -1, -2]]
CLAUSES[(3, 157)] = [[2, -3], [3, -1, -2]]
CLAUSES[(3, 158)] = [[1, 2, 3], [2, -1, -3], [3, -1, -2]]
CLAUSES[(3, 159)] = [[2, -1, -3], [3, -1, -2]]
CLAUSES[(3, 160)] = [[1], [3]]
CLAUSES[(3, 161)] = [[1, -2], [1, -3], [3, -1]]
CLAUSES[(3, 162)] = [[3], [1, -2]]
CLAUSES[(3, 163)] = [[1, -2], [3, -1]]
CLAUSES[(3, 164)] = [[1, 2], [1, -3], [3, -1]]
CLAUSES[(3, 165)] = [[1, -3], [3, -1]]
CLAUSES[(3, 166)] = [[2, 3], [3, -1], [1, -2, -3]]
CLAUSES[(3, 167)] = [[3, -1], [1, -2, -3]]
CLAUSES[(3, 168)] = [[3], [1, 2]]
CLAUSES[(3, 169)] = [[3, -1], [3, -2], [1, 2, -3]]
CLAUSES[(3, 170)] = [[3]]
CLAUSES[(3, 171)] = [[3, -1], [3, -2]]
CLAUSES[(3, 172)] = [[1, 2], [3, -1]]
CLAUSES[(3, 173)] = [[3, -1], [1, 2, -3]]
CLAUSES[(3, 174)] = [[2, 3], [3, -1]]
CLAUSES[(3, 175)] = [[3, -1]]
CLAUSES[(3, 176)] = [[1], [3, -2]]
CLAUSES[(3, 177)] = [[1, -3], [3, -2]]
CLAUSES[(3, 178)] = [[1, 3], [1, -2], [3, -2]]
CLAUSES[(3, 179)] = [[1, -2], [3, -2]]
CLAUSES[(3, 180)] = [[1, 2], [1, -3], [3, -1, -2]]
CLAUSES[(3, 181)] = [[1, -3], [3, -1, -2]]
CLAUSES[(3, 182)] = [[1, 2, 3], [1, -2, -3], [3, -1, -2]]
CLAUSES[(3, 183)] = [[1, -2, -3], [3, -1, -2]]
CLAUSES[(3, 184)] = [[1, 2], [3, -2]]
CLAUSES[(3, 185)] = [[3, -2], [1, 2, -3]]
CLAUSES[(3, 186)] = [[1, 3], [3, -2]]
CLAUSES[(3, 187)] = [[3, -2]]
CLAUSES[(3, 188)] = [[1, 2], [3, -1, -2]]
CLAUSES[(3, 189)] = [[1, 2, -3], [3, -1, -2]]
CLAUSES[(3, 190)] = [[1, 2, 3], [3, -1, -2]]
CLAUSES[(3, 191)] = [[3, -1, -2]]
CLAUSES[(3, 192)] = [[1], [2]]
CLAUSES[(3, 193)] = [[1, -2], [1, -3], [2, -1]]
CLAUSES[(3, 194)] = [[1, 3], [1, -2], [2, -1]]
CLAUSES[(3, 195)] = [[1, -2], [2, -1]]
CLAUSES[(3, 196)] = [[2], [1, -3]]
CLAUSES[(3, 197)] = [[1, -3], [2, -1]]
CLAUSES[(3, 198)] = [[2, 3], [2, -1], [1, -2, -3]]
CLAUSES[(3, 199)] = [[2, -1], [1, -2, -3]]
CLAUSES[(3, 200)] = [[2], [1, 3]]
CLAUSES[(3, 201)] = [[2, -1], [2, -3], [1, 3, -2]]
CLAUSES[(3, 202)] = [[1, 3], [2, -1]]
CLAUSES[(3, 203)] = [[2, -1], [1, 3, -2]]
CLAUSES[(3, 204)] = [[2]]
CLAUSES[(3, 205)] = [[2, -1], [2, -3]]
CLAUSES[(3, 206)] = [[2, 3], [2, -1]]
CLAUSES[(3, 207)] = [[2, -1]]
CLAUSES[(3, 208)] = [[1], [2, -3]]
CLAUSES[(3, 209)] = [[1, -2], [2, -3]]
CLAUSES[(3, 210)] = [[1, 3], [1, -2], [2, -1, -3]]
CLAUSES[(3, 211)] = [[1, -2], [2, -1, -3]]
CLAUSES[(3, 212)] = [[1, 2], [1, -3], [2, -3]]
CLAUSES[(3, 213)] = [[1, -3], [2, -3]]
CLAUSES[(3, 214)] = [[1, 2, 3], [1, -2, -3], [2, -1, -3]]
CLAUSES[(3, 215)] = [[1, -2, -3], [2, -1, -3]]
CLAUSES[(3, 216)] = [[1, 3], [2, -3]]
CLAUSES[(3, 217)] = [[2, -3], [1, 3, -2]]
CLAUSES[(3, 218)] = [[1, 3], [2, -1, -3]]
CLAUSES[(3, 219)] = [[1, 3, -2], [2, -1, -3]]
CLAUSES[(3, 220)] = [[1, 2], [2, -3]]
CLAUSES[(3, 221)] = [[2, -3]]
CLAUSES[(3, 222)] = [[1, 2, 3], [2, -1, -3]]
CLAUSES[(3, 223)] = [[2, -1, -3]]
CLAUSES[(3, 224)] = [[1], [2, 3]]
CLAUSES[(3, 225)] = [[1, -2], [1, -3], [2, 3, -1]]
CLAUSES[(3, 226)] = [[2, 3], [1, -2]]
CLAUSES[(3, 227)] = [[1, -2], [2, 3, -1]]
CLAUSES[(3, 228)] = [[2, 3], [1, -3]]
CLAUSES[(3, 229)] = [[1, -3], [2, 3, -1]]
CLAUSES[(3, 230)] = [[2, 3], [1, -2, -3]]
CLAUSES[(3, 231)] = [[2, 3, -1], [1, -2, -3]]
CLAUSES[(3, 232)] = [[1, 2], [1, 3], [2, 3]]
CLAUSES[(3, 233)] = [[1, 2, -3], [1, 3, -2], [2, 3, -1]]
CLAUSES[(3, 234)] = [[1, 3], [2, 3]]
CLAUSES[(3, 235)] = [[1, 3, -2], [2, 3, -1]]
CLAUSES[(3, 236)] = [[1, 2], [2, 3]]
CLAUSES[(3, 237)] = [[1, 2, -3], [2, 3, -1]]
CLAUSES[(3, 238)] = [[2, 3]]
CLAUSES[(3, 239)] = [[2, 3, -1]]
CLAUSES[(3, 240)] = [[1]]
CLAUSES[(3, 241)] = [[1, -2], [1, -3]]
CLAUSES[(3, 242)] = [[1, 3], [1, -2]]
CLAUSES[(3, 243)] = [[1, -2]]
CLAUSES[(3, 244)] = [[1, 2], [1, -3]]
CLAUSES[(3, 245)] = [[1, -3]]
CLAUSES[(3, 246)] = [[1, 2, 3], [1, -2, -3]]
CLAUSES[(3, 247)] = [[1, -2, -3]]
CLAUSES[(3, 248)] = [[1, 2], [1, 3]]
CLAUSES[(3, 249)] = [[1, 2, -3], [1, 3, -2]]
CLAUSES[(3, 250)] = [[1, 3]]
CLAUSES[(3, 251)] = [[1, 3, -2]]
CLAUSES[(3, 252)] = [[1, 2]]
CLAUSES[(3, 253)] = [[1, 2, -3]]
CLAUSES[(3, 254)] = [[1, 2, 3]]
CLAUSES[(3, 255)] = []

class Var:
    '''
    A boolean variable in a boolean expression.
    '''

    def __init__ (self, expression, index, name):
        self.__index = index
        self.__expression = expression
        self.__name = name

    expression = property(lambda self: self.__expression)

    index = property(lambda self: self.__index)

    name = property(lambda self: self.__name)

    def __repr__ (self):
        return self.__str__()

    def __str__ (self):
        return self.name

    def __invert__(self):
        return Not(self)

    def __and__(self, other):
        return And(self, other)

    def __or__(self, other):
        return Or(self, other)

    def __xor__(self, other):
        return Xor(self, other)

class BooleanExpression:
    '''
    A boolean expression consisting of variables and 3-CNF clauses.
    '''

    def __init__ (self, solver):
        self.__solver = solver
        self.__counter = 1
        self.__variables = dict()
        self.__variables_reverse = dict()

    def __getitem__ (self, name) -> Var:
        if name in self.__variables_reverse:
            return self.__variables_reverse[name]
        if name not in self.__variables:
            self.add_var(name)
        return self.__variables[name]

    def add_var (self, name=None) -> Var:
        index = self.__counter
        name = f"${index}" if name is None else name
        if name in self.__variables: raise ValueError(f"duplicate variable: {name}")
        variable = Var(self, index, name)
        self.__counter += 1
        self.__variables[name] = variable
        self.__variables_reverse[index] = variable
        return variable

    def add_clause (self, x : int, y : int = None, z : int = None):
        assert isinstance(x, int)
        assert isinstance(y, int) or (y is None)
        assert isinstance(z, int) or (z is None)
        if (x is not None) and (y is not None) and (z is not None):
            clause = tuple([x, y, z])
            self.solver.add_clause(clause)
        elif (x is not None) and (y is not None):
            clause = tuple([x, y])
            self.solver.add_clause(clause)
        else: # (x is not None):
            clause = tuple([x])
            self.solver.add_clause(clause)

    def solve (self, *args, **kwargs):
        return self.solver.solve(*args, **kwargs)

    def get_model (self, *args, **kwargs):
        result = [(None, None) for n in range(0, len(self.__variables))]
        # The solver does not necessarily know about all of the variables.
        # If a variable was declared, by not used in a clause,
        # then it is a "don't care" from the perspective of solver.
        # We still want the variable in the model, but assigned null.
        # So, to start, lets make sure that every variable is at
        # least assigned to node in the result.
        for index, variable in self.__variables_reverse.items():
            index = abs(index) - 1 # vars are one-based
            result[index] = (variable, None)
        # Then, for the variables that were actually assigned
        # values by the solver, replace the placeholder nulls
        # with the real values assigned by the solver.
        for assignment in self.solver.get_model(*args, **kwargs):
            value = assignment >= 0
            index = abs(assignment)
            variable = self.__variables_reverse[index]
            index -= 1 # vars are one-based
            result[index] = (variable, value)
        return result

    solver = property(lambda self: self.__solver)

    variables = property(lambda self: list(self.__variables.values()))

def Fn (n : int, x : Var, y : Var = None, z : Var = None):
    if (x is not None) and (y is not None) and (z is not None):
        expression = x.expression
        for clause in CLAUSES[(3, n)]:
            X = x.index
            Y = y.index
            Z = z.index
            lookup = {
                +1: +X,
                -1: -X,
                +2: +Y,
                -2: -Y,
                +3: +Z,
                -3: -Z,
            }
            clause = [lookup[m] for m in clause]
            expression.add_clause(*clause)
    elif (x is not None) and (y is not None):
        expression = x.expression
        for clause in CLAUSES[(2, n)]:
            X = x.index
            Y = y.index
            lookup = {
                +1: +X,
                -1: -X,
                +2: +Y,
                -2: -Y
            }
            clause = [lookup[m] for m in clause]
            expression.add_clause(*clause)
    else: # (x is not None):
        expression = x.expression
        for clause in CLAUSES[(1, n)]:
            X = x.index
            lookup = {
                +1: +X,
                -1: -X
            }
            clause = [lookup[m] for m in clause]
            expression.add_clause(*clause)


def UNSAT (x : Var):
    '''
    See on Wolfram Alpha: BooleanFunction[0, 1]
    '''
    Fn(0, x)

def FALSE (x : Var):
    '''
    See on Wolfram Alpha: BooleanFunction[1, 1]
    '''
    Fn(1, x)

def TRUE (x : Var):
    '''
    See on Wolfram Alpha: BooleanFunction[2, 1]
    '''
    Fn(2, x)

def VARIES (x : Var):
    '''
    See on Wolfram Alpha: BooleanFunction[3, 1]
    '''
    Fn(3, x)


def NOR (x : Var, y : Var):
    '''
    See on Wolfram Alpha: BooleanFunction[1, 2]
    '''
    Fn(1, x, y)

def NIMPLY (x : Var, y : Var):
    '''
    See on Wolfram Alpha: BooleanFunction[4, 2]
    '''
    Fn(4, x, y)

def XOR (x : Var, y : Var):
    '''
    See on Wolfram Alpha: BooleanFunction[6, 2]
    '''
    Fn(6, x, y)

def NAND (x : Var, y : Var):
    '''
    See on Wolfram Alpha: BooleanFunction[7, 2]
    '''
    Fn(7, x, y)

def AND (x : Var, y : Var):
    '''
    See on Wolfram Alpha: BooleanFunction[8, 2]
    '''
    Fn(8, x, y)

def XNOR (x : Var, y : Var):
    '''
    See on Wolfram Alpha: BooleanFunction[9, 2]
    '''
    Fn(9, x, y)

def IMPLIES (x : Var, y : Var):
    '''
    See on Wolfram Alpha: BooleanFunction[11, 2]
    '''
    Fn(11, x, y)

def CONVERSE (x : Var, y : Var):
    '''
    See on Wolfram Alpha: BooleanFunction[13, 2]
    '''
    Fn(13, x, y)

def OR (x : Var, y : Var):
    '''
    See on Wolfram Alpha: BooleanFunction[14, 2]
    '''
    Fn(14, x, y)

def IMPLIES_NOT (x : Var, y : Var):
    '''
    Alias of NAND.
    '''
    NAND(x, y)

def IFF (x : Var, y : Var):
    '''
    Alias of XNOR.
    '''
    XNOR(x, y)

def Not (x : Var, y : Var = None) -> Var:
    '''
    See on Wolfram Alpha: BooleanFunction[6, 2]
    '''
    y = x.expression.add_var() if y is None else y
    XOR(x, y)
    return y

def And (x : Var, y : Var, z : Var = None) -> Var:
    '''
    See on Wolfram Alpha: BooleanFunction[149, 3]
    '''
    z = x.expression.add_var() if z is None else z
    Fn(149, x, y, z)
    return z

def Or (x : Var, y : Var, z : Var = None) -> Var:
    '''
    See on Wolfram Alpha: BooleanFunction[169, 3]
    '''
    z = x.expression.add_var() if z is None else z
    Fn(169, x, y, z)
    return z

def Xor (x : Var, y : Var, z : Var = None) -> Var:
    '''
    See on Wolfram Alpha: BooleanFunction[105, 3]
    '''
    z = x.expression.add_var() if z is None else z
    Fn(105, x, y, z)
    return z

def Xnor (x : Var, y : Var, z : Var = None) -> Var:
    '''
    See on Wolfram Alpha: BooleanFunction[150, 3]
    '''
    z = x.expression.add_var() if z is None else z
    Fn(150, x, y, z)
    return z

def Nand (x : Var, y : Var, z : Var = None) -> Var:
    '''
    See on Wolfram Alpha: BooleanFunction[106, 3]
    '''
    z = x.expression.add_var() if z is None else z
    Fn(106, x, y, z)
    return z

def Nor (x : Var, y : Var, z : Var = None) -> Var:
    '''
    See on Wolfram Alpha: BooleanFunction[86, 3]
    '''
    z = x.expression.add_var() if z is None else z
    Fn(86, x, y, z)
    return z

def Nimply (x : Var, y : Var, z : Var = None) -> Var:
    '''
    See on Wolfram Alpha: BooleanFunction[101, 3]
    '''
    z = x.expression.add_var() if z is None else z
    Fn(101, x, y, z)
    return z

def Implies (x : Var, y : Var, z : Var = None) -> Var:
    '''
    See on Wolfram Alpha: BooleanFunction[154, 3]
    '''
    z = x.expression.add_var() if z is None else z
    Fn(154, x, y, z)
    return z

def ImpliesNot (x : Var, y : Var, z : Var = None) -> Var:
    '''
    See on Wolfram Alpha: BooleanFunction[106, 3]
    '''
    z = x.expression.add_var() if z is None else z
    Fn(106, x, y, z)
    return z

def Converse (x : Var, y : Var, z : Var = None) -> Var:
    '''
    See on Wolfram Alpha: BooleanFunction[166, 3]
    '''
    z = x.expression.add_var() if z is None else z
    Fn(166, x, y, z)
    return z

def Iff (x : Var, y : Var, z : Var = None) -> Var:
    '''
    Alias of Xnor().
    '''
    return Xnor(x, y, z=z)

def assign (target : Var, value : bool):
    '''
    Constrain a variable to either true or false.
    '''
    if value:
        TRUE(target)
    else:
        FALSE(target)

# This is a reminder to myself not to import pysat directly.
# I want this module to remain generic and rely on the absolute
# minimum of the pysat API, so that it is easier/possible to
# reuse this module with other SAT solver implementations
# that are not part of the pysat ecosystem.
# Therefore, this module only really relies on  solvers:
# 1. having an add_clause() method,
# 2. having a solve() method,
# 3. having a get_model() method,
# where those methods are compatible with pysat.
assert 'pysat' not in locals(), "pysat imported"

#
# Copyright (c) 2024 Mackenzie High. All rights reserved.
#
