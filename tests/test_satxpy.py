#
# Copyright (c) 2024 Mackenzie High. All rights reserved.
#

import unittest

from src.satxpy import *
from pysat.solvers import Glucose3

T = True
F = False

class UnitTest (unittest.TestCase):

    def check_truth_table (self, whenSAT, constrain, satisfiable, args):
        solver = Glucose3()
        expr = BooleanExpression(solver)
        arity = len(args)
        if arity == 1:
            A = expr["A"]
            vargs = [A]
            assign(A, args[0])
        elif arity == 2:
            A = expr["A"]
            B = expr["B"]
            vargs = [A, B]
            assign(A, args[0])
            assign(B, args[1])
        elif arity == 3:
            A = expr["A"]
            B = expr["B"]
            C = expr["C"]
            vargs = [A, B, C]
            assign(A, args[0])
            assign(B, args[1])
            assign(C, args[2])
        constrain(expr, *vargs)
        output = expr.solve()
        self.assertEqual(satisfiable, output)
        if whenSAT:
            if satisfiable:
                whenSAT(*args)

    def test_UNSAT (self):
        def constrain (expr, x):
            UNSAT(x)
        def whenSAT (x):
            pass
        self.check_truth_table(whenSAT, constrain, F, [T]) # 1
        self.check_truth_table(whenSAT, constrain, F, [F]) # 0

    def test_FALSE (self):
        def constrain (expr, x):
            FALSE(x)
        def whenSAT (x):
            pass
        self.check_truth_table(whenSAT, constrain, F, [T]) # 1
        self.check_truth_table(whenSAT, constrain, T, [F]) # 0

    def test_TRUE (self):
        def constrain (expr, x):
            TRUE(x)
        def whenSAT (x):
            pass
        self.check_truth_table(whenSAT, constrain, T, [T]) # 1
        self.check_truth_table(whenSAT, constrain, F, [F]) # 0

    def test_VARIES (self):
        def constrain (expr, x):
            VARIES(x)
        def whenSAT (x):
            pass
        self.check_truth_table(whenSAT, constrain, T, [T]) # 1
        self.check_truth_table(whenSAT, constrain, T, [F]) # 0

    def test_NOR (self):
        def constrain (expr, x, y):
            NOR(x, y)
        def whenSAT (x, y):
            self.assertTrue(not (x or y))
        self.check_truth_table(whenSAT, constrain, F, [T, T]) # 3
        self.check_truth_table(whenSAT, constrain, F, [T, F]) # 2
        self.check_truth_table(whenSAT, constrain, F, [F, T]) # 1
        self.check_truth_table(whenSAT, constrain, T, [F, F]) # 0

    def test_NIMPLY (self):
        def constrain (expr, x, y):
            NIMPLY(x, y)
        def whenSAT (x, y):
            self.assertTrue(x and not y)
        self.check_truth_table(whenSAT, constrain, F, [T, T]) # 3
        self.check_truth_table(whenSAT, constrain, T, [T, F]) # 2
        self.check_truth_table(whenSAT, constrain, F, [F, T]) # 1
        self.check_truth_table(whenSAT, constrain, F, [F, F]) # 0

    def test_XOR (self):
        def constrain (expr, x, y):
            XOR(x, y)
        def whenSAT (x, y):
            self.assertTrue(x ^ y)
        self.check_truth_table(whenSAT, constrain, F, [T, T]) # 3
        self.check_truth_table(whenSAT, constrain, T, [T, F]) # 2
        self.check_truth_table(whenSAT, constrain, T, [F, T]) # 1
        self.check_truth_table(whenSAT, constrain, F, [F, F]) # 0

    def test_NAND (self):
        def constrain (expr, x, y):
            NAND(x, y)
        def whenSAT (x, y):
            self.assertTrue(not (x and y))
        self.check_truth_table(whenSAT, constrain, F, [T, T]) # 3
        self.check_truth_table(whenSAT, constrain, T, [T, F]) # 2
        self.check_truth_table(whenSAT, constrain, T, [F, T]) # 1
        self.check_truth_table(whenSAT, constrain, T, [F, F]) # 0

    def test_AND (self):
        def constrain (expr, x, y):
            AND(x, y)
        def whenSAT (x, y):
            self.assertTrue(x and y)
        self.check_truth_table(whenSAT, constrain, T, [T, T]) # 3
        self.check_truth_table(whenSAT, constrain, F, [T, F]) # 2
        self.check_truth_table(whenSAT, constrain, F, [F, T]) # 1
        self.check_truth_table(whenSAT, constrain, F, [F, F]) # 0

    def test_XNOR (self):
        def constrain (expr, x, y):
            XNOR(x, y)
        def whenSAT (x, y):
            self.assertTrue(x == y)
        self.check_truth_table(whenSAT, constrain, T, [T, T]) # 3
        self.check_truth_table(whenSAT, constrain, F, [T, F]) # 2
        self.check_truth_table(whenSAT, constrain, F, [F, T]) # 1
        self.check_truth_table(whenSAT, constrain, T, [F, F]) # 0

    def test_IMPLIES (self):
        def constrain (expr, x, y):
            IMPLIES(x, y)
        def whenSAT (x, y):
            self.assertTrue((not x) or y)
        self.check_truth_table(whenSAT, constrain, T, [T, T]) # 3
        self.check_truth_table(whenSAT, constrain, F, [T, F]) # 2
        self.check_truth_table(whenSAT, constrain, T, [F, T]) # 1
        self.check_truth_table(whenSAT, constrain, T, [F, F]) # 0

    def test_IMPLIES_NOT (self):
        def constrain (expr, x, y):
            IMPLIES_NOT(x, y)
        def whenSAT (x, y):
            self.assertTrue((not x) or (not y))
        self.check_truth_table(whenSAT, constrain, F, [T, T]) # 3
        self.check_truth_table(whenSAT, constrain, T, [T, F]) # 2
        self.check_truth_table(whenSAT, constrain, T, [F, T]) # 1
        self.check_truth_table(whenSAT, constrain, T, [F, F]) # 0

    def test_CONVERSE (self):
        def constrain (expr, x, y):
            CONVERSE(x, y)
        def whenSAT (x, y):
            self.assertTrue(x or (not y))
        self.check_truth_table(whenSAT, constrain, T, [T, T]) # 3
        self.check_truth_table(whenSAT, constrain, T, [T, F]) # 2
        self.check_truth_table(whenSAT, constrain, F, [F, T]) # 1
        self.check_truth_table(whenSAT, constrain, T, [F, F]) # 0

    def test_OR (self):
        def constrain (expr, x, y):
            OR(x, y)
        def whenSAT (x, y):
            self.assertTrue(x or y)
        self.check_truth_table(whenSAT, constrain, T, [T, T]) # 3
        self.check_truth_table(whenSAT, constrain, T, [T, F]) # 2
        self.check_truth_table(whenSAT, constrain, T, [F, T]) # 1
        self.check_truth_table(whenSAT, constrain, F, [F, F]) # 0

    def test_IFF (self):
        def constrain (expr, x, y):
            IFF(x, y)
        def whenSAT (x, y):
            self.assertTrue(x == y)
        self.check_truth_table(whenSAT, constrain, T, [T, T]) # 3
        self.check_truth_table(whenSAT, constrain, F, [T, F]) # 2
        self.check_truth_table(whenSAT, constrain, F, [F, T]) # 1
        self.check_truth_table(whenSAT, constrain, T, [F, F]) # 0

    def test_Not (self):
        def constrain (expr, x, y):
            out = Not(x, y)
            self.assertIs(y, out)
        def whenSAT (x, y):
            self.assertEqual(y, not x)
        self.check_truth_table(whenSAT, constrain, F, [T, T]) # 3
        self.check_truth_table(whenSAT, constrain, T, [T, F]) # 2
        self.check_truth_table(whenSAT, constrain, T, [F, T]) # 1
        self.check_truth_table(whenSAT, constrain, F, [F, F]) # 0

    def test_Not_operator (self):
        def constrain (expr, x, y):
            out = ~x
            # Hold y = out, since cannot pass y into the operator.
            IFF(y, out)
        def whenSAT (x, y):
            self.assertEqual(y, not x)
        self.check_truth_table(whenSAT, constrain, F, [T, T]) # 3
        self.check_truth_table(whenSAT, constrain, T, [T, F]) # 2
        self.check_truth_table(whenSAT, constrain, T, [F, T]) # 1
        self.check_truth_table(whenSAT, constrain, F, [F, F]) # 0

    def test_And (self):
        def constrain (expr, x, y, z):
            out = And(x, y, z)
            self.assertIs(z, out)
        def whenSAT (x, y, z):
            self.assertEqual(z, x and y)
        self.check_truth_table(whenSAT, constrain, T, [T, T, T]) # 7
        self.check_truth_table(whenSAT, constrain, F, [T, T, F]) # 6
        self.check_truth_table(whenSAT, constrain, F, [T, F, T]) # 5
        self.check_truth_table(whenSAT, constrain, T, [T, F, F]) # 4
        self.check_truth_table(whenSAT, constrain, F, [F, T, T]) # 3
        self.check_truth_table(whenSAT, constrain, T, [F, T, F]) # 2
        self.check_truth_table(whenSAT, constrain, F, [F, F, T]) # 1
        self.check_truth_table(whenSAT, constrain, T, [F, F, F]) # 0

    def test_And_operator (self):
        def constrain (expr, x, y, z):
            out = x & y
            # Hold z = out, since cannot pass z into the operator.
            IFF(z, out)
        def whenSAT (x, y, z):
            self.assertEqual(z, x and y)
        self.check_truth_table(whenSAT, constrain, T, [T, T, T]) # 7
        self.check_truth_table(whenSAT, constrain, F, [T, T, F]) # 6
        self.check_truth_table(whenSAT, constrain, F, [T, F, T]) # 5
        self.check_truth_table(whenSAT, constrain, T, [T, F, F]) # 4
        self.check_truth_table(whenSAT, constrain, F, [F, T, T]) # 3
        self.check_truth_table(whenSAT, constrain, T, [F, T, F]) # 2
        self.check_truth_table(whenSAT, constrain, F, [F, F, T]) # 1
        self.check_truth_table(whenSAT, constrain, T, [F, F, F]) # 0

    def test_Or (self):
        def constrain (expr, x, y, z):
            out = Or(x, y, z)
            self.assertIs(z, out)
        def whenSAT (x, y, z):
            self.assertEqual(z, x or y)
        self.check_truth_table(whenSAT, constrain, T, [T, T, T]) # 7
        self.check_truth_table(whenSAT, constrain, F, [T, T, F]) # 6
        self.check_truth_table(whenSAT, constrain, T, [T, F, T]) # 5
        self.check_truth_table(whenSAT, constrain, F, [T, F, F]) # 4
        self.check_truth_table(whenSAT, constrain, T, [F, T, T]) # 3
        self.check_truth_table(whenSAT, constrain, F, [F, T, F]) # 2
        self.check_truth_table(whenSAT, constrain, F, [F, F, T]) # 1
        self.check_truth_table(whenSAT, constrain, T, [F, F, F]) # 0

    def test_Or_operator (self):
        def constrain (expr, x, y, z):
            out = x | y
            # Hold z = out, since cannot pass z into the operator.
            IFF(z, out)
        def whenSAT (x, y, z):
            self.assertEqual(z, x or y)
        self.check_truth_table(whenSAT, constrain, T, [T, T, T]) # 7
        self.check_truth_table(whenSAT, constrain, F, [T, T, F]) # 6
        self.check_truth_table(whenSAT, constrain, T, [T, F, T]) # 5
        self.check_truth_table(whenSAT, constrain, F, [T, F, F]) # 4
        self.check_truth_table(whenSAT, constrain, T, [F, T, T]) # 3
        self.check_truth_table(whenSAT, constrain, F, [F, T, F]) # 2
        self.check_truth_table(whenSAT, constrain, F, [F, F, T]) # 1
        self.check_truth_table(whenSAT, constrain, T, [F, F, F]) # 0

    def test_Xor (self):
        def constrain (expr, x, y, z):
            out = Xor(x, y, z)
            self.assertIs(z, out)
        def whenSAT (x, y, z):
            self.assertEqual(z, x ^ y)
        self.check_truth_table(whenSAT, constrain, F, [T, T, T]) # 7
        self.check_truth_table(whenSAT, constrain, T, [T, T, F]) # 6
        self.check_truth_table(whenSAT, constrain, T, [T, F, T]) # 5
        self.check_truth_table(whenSAT, constrain, F, [T, F, F]) # 4
        self.check_truth_table(whenSAT, constrain, T, [F, T, T]) # 3
        self.check_truth_table(whenSAT, constrain, F, [F, T, F]) # 2
        self.check_truth_table(whenSAT, constrain, F, [F, F, T]) # 1
        self.check_truth_table(whenSAT, constrain, T, [F, F, F]) # 0

    def test_Xor_operator (self):
        def constrain (expr, x, y, z):
            out = x ^ y
            # Hold z = out, since cannot pass z into the operator.
            IFF(z, out)
        def whenSAT (x, y, z):
            self.assertEqual(z, x ^ y)
        self.check_truth_table(whenSAT, constrain, F, [T, T, T]) # 7
        self.check_truth_table(whenSAT, constrain, T, [T, T, F]) # 6
        self.check_truth_table(whenSAT, constrain, T, [T, F, T]) # 5
        self.check_truth_table(whenSAT, constrain, F, [T, F, F]) # 4
        self.check_truth_table(whenSAT, constrain, T, [F, T, T]) # 3
        self.check_truth_table(whenSAT, constrain, F, [F, T, F]) # 2
        self.check_truth_table(whenSAT, constrain, F, [F, F, T]) # 1
        self.check_truth_table(whenSAT, constrain, T, [F, F, F]) # 0

    def test_Xnor (self):
        def constrain (expr, x, y, z):
            out = Xnor(x, y, z)
            self.assertIs(z, out)
        def whenSAT (x, y, z):
            self.assertEqual(z, x == y)
        self.check_truth_table(whenSAT, constrain, T, [T, T, T]) # 7
        self.check_truth_table(whenSAT, constrain, F, [T, T, F]) # 6
        self.check_truth_table(whenSAT, constrain, F, [T, F, T]) # 5
        self.check_truth_table(whenSAT, constrain, T, [T, F, F]) # 4
        self.check_truth_table(whenSAT, constrain, F, [F, T, T]) # 3
        self.check_truth_table(whenSAT, constrain, T, [F, T, F]) # 2
        self.check_truth_table(whenSAT, constrain, T, [F, F, T]) # 1
        self.check_truth_table(whenSAT, constrain, F, [F, F, F]) # 0

    def test_Nand (self):
        def constrain (expr, x, y, z):
            out = Nand(x, y, z)
            self.assertIs(z, out)
        def whenSAT (x, y, z):
            self.assertEqual(z, not (x and y))
        self.check_truth_table(whenSAT, constrain, F, [T, T, T]) # 7
        self.check_truth_table(whenSAT, constrain, T, [T, T, F]) # 6
        self.check_truth_table(whenSAT, constrain, T, [T, F, T]) # 5
        self.check_truth_table(whenSAT, constrain, F, [T, F, F]) # 4
        self.check_truth_table(whenSAT, constrain, T, [F, T, T]) # 3
        self.check_truth_table(whenSAT, constrain, F, [F, T, F]) # 2
        self.check_truth_table(whenSAT, constrain, T, [F, F, T]) # 1
        self.check_truth_table(whenSAT, constrain, F, [F, F, F]) # 0

    def test_Nor (self):
        def constrain (expr, x, y, z):
            out = Nor(x, y, z)
            self.assertIs(z, out)
        def whenSAT (x, y, z):
            self.assertEqual(z, not (x or y))
        self.check_truth_table(whenSAT, constrain, F, [T, T, T]) # 7
        self.check_truth_table(whenSAT, constrain, T, [T, T, F]) # 6
        self.check_truth_table(whenSAT, constrain, F, [T, F, T]) # 5
        self.check_truth_table(whenSAT, constrain, T, [T, F, F]) # 4
        self.check_truth_table(whenSAT, constrain, F, [F, T, T]) # 3
        self.check_truth_table(whenSAT, constrain, T, [F, T, F]) # 2
        self.check_truth_table(whenSAT, constrain, T, [F, F, T]) # 1
        self.check_truth_table(whenSAT, constrain, F, [F, F, F]) # 0

    def test_Nimply (self):
        def constrain (expr, x, y, z):
            out = Nimply(x, y, z)
            self.assertIs(z, out)
        def whenSAT (x, y, z):
            self.assertEqual(z, x and (not y))
        self.check_truth_table(whenSAT, constrain, F, [T, T, T]) # 7
        self.check_truth_table(whenSAT, constrain, T, [T, T, F]) # 6
        self.check_truth_table(whenSAT, constrain, T, [T, F, T]) # 5
        self.check_truth_table(whenSAT, constrain, F, [T, F, F]) # 4
        self.check_truth_table(whenSAT, constrain, F, [F, T, T]) # 3
        self.check_truth_table(whenSAT, constrain, T, [F, T, F]) # 2
        self.check_truth_table(whenSAT, constrain, F, [F, F, T]) # 1
        self.check_truth_table(whenSAT, constrain, T, [F, F, F]) # 0

    def test_Implies (self):
        def constrain (expr, x, y, z):
            out = Implies(x, y, z)
            self.assertIs(z, out)
        def whenSAT (x, y, z):
            self.assertEqual(z, (not x) or y)
        self.check_truth_table(whenSAT, constrain, T, [T, T, T]) # 7
        self.check_truth_table(whenSAT, constrain, F, [T, T, F]) # 6
        self.check_truth_table(whenSAT, constrain, F, [T, F, T]) # 5
        self.check_truth_table(whenSAT, constrain, T, [T, F, F]) # 4
        self.check_truth_table(whenSAT, constrain, T, [F, T, T]) # 3
        self.check_truth_table(whenSAT, constrain, F, [F, T, F]) # 2
        self.check_truth_table(whenSAT, constrain, T, [F, F, T]) # 1
        self.check_truth_table(whenSAT, constrain, F, [F, F, F]) # 0

    def test_ImpliesNot (self):
        def constrain (expr, x, y, z):
            out = ImpliesNot(x, y, z)
            self.assertIs(z, out)
        def whenSAT (x, y, z):
            self.assertEqual(z, (not x) or (not y))
        self.check_truth_table(whenSAT, constrain, F, [T, T, T]) # 7
        self.check_truth_table(whenSAT, constrain, T, [T, T, F]) # 6
        self.check_truth_table(whenSAT, constrain, T, [T, F, T]) # 5
        self.check_truth_table(whenSAT, constrain, F, [T, F, F]) # 4
        self.check_truth_table(whenSAT, constrain, T, [F, T, T]) # 3
        self.check_truth_table(whenSAT, constrain, F, [F, T, F]) # 2
        self.check_truth_table(whenSAT, constrain, T, [F, F, T]) # 1
        self.check_truth_table(whenSAT, constrain, F, [F, F, F]) # 0

    def test_Converse (self):
        def constrain (expr, x, y, z):
            out = Converse(x, y, z)
            self.assertIs(z, out)
        def whenSAT (x, y, z):
            self.assertEqual(z, x or (not y))
        self.check_truth_table(whenSAT, constrain, T, [T, T, T]) # 7
        self.check_truth_table(whenSAT, constrain, F, [T, T, F]) # 6
        self.check_truth_table(whenSAT, constrain, T, [T, F, T]) # 5
        self.check_truth_table(whenSAT, constrain, F, [T, F, F]) # 4
        self.check_truth_table(whenSAT, constrain, F, [F, T, T]) # 3
        self.check_truth_table(whenSAT, constrain, T, [F, T, F]) # 2
        self.check_truth_table(whenSAT, constrain, T, [F, F, T]) # 1
        self.check_truth_table(whenSAT, constrain, F, [F, F, F]) # 0

    def test_Iff (self):
        def constrain (expr, x, y, z):
            out = Iff(x, y, z)
            self.assertIs(z, out)
        def whenSAT (x, y, z):
            self.assertEqual(z, x == y)
        self.check_truth_table(whenSAT, constrain, T, [T, T, T]) # 7
        self.check_truth_table(whenSAT, constrain, F, [T, T, F]) # 6
        self.check_truth_table(whenSAT, constrain, F, [T, F, T]) # 5
        self.check_truth_table(whenSAT, constrain, T, [T, F, F]) # 4
        self.check_truth_table(whenSAT, constrain, F, [F, T, T]) # 3
        self.check_truth_table(whenSAT, constrain, T, [F, T, F]) # 2
        self.check_truth_table(whenSAT, constrain, T, [F, F, T]) # 1
        self.check_truth_table(whenSAT, constrain, F, [F, F, F]) # 0

    def test_Fn_with_arity_1 (self):
        for n in range(0, 4):
            S0 = (n >> 0) & 1
            S1 = (n >> 1) & 1
            def constrain (expr, x):
                Fn(n, x)
            def whenSAT (x):
                pass
            self.assertEqual(n, (S1 * 2**1) +  (S0 * 2**0))
            self.check_truth_table(whenSAT, constrain, S1, [T]) # 1
            self.check_truth_table(whenSAT, constrain, S0, [F]) # 0

    def test_Fn_with_arity_2 (self):
        for n in range(0, 16):
            S0 = (n >> 0) & 1
            S1 = (n >> 1) & 1
            S2 = (n >> 2) & 1
            S3 = (n >> 3) & 1
            def constrain (expr, x, y):
                Fn(n, x, y)
            def whenSAT (x, y):
                pass
            self.assertEqual(n, (S3 * 2**3)
                             +  (S2 * 2**2)
                             +  (S1 * 2**1)
                             +  (S0 * 2**0))
            self.check_truth_table(whenSAT, constrain, S3, [T, T]) # 3
            self.check_truth_table(whenSAT, constrain, S2, [T, F]) # 2
            self.check_truth_table(whenSAT, constrain, S1, [F, T]) # 1
            self.check_truth_table(whenSAT, constrain, S0, [F, F]) # 0

    def test_Fn_with_arity_3 (self):
        for n in range(0, 256):
            S0 = (n >> 0) & 1
            S1 = (n >> 1) & 1
            S2 = (n >> 2) & 1
            S3 = (n >> 3) & 1
            S4 = (n >> 4) & 1
            S5 = (n >> 5) & 1
            S6 = (n >> 6) & 1
            S7 = (n >> 7) & 1
            def constrain (expr, x, y, z):
                Fn(n, x, y, z)
            def whenSAT (x, y, z):
                pass
            self.assertEqual(n, (S7 * 2**7)
                             +  (S6 * 2**6)
                             +  (S5 * 2**5)
                             +  (S4 * 2**4)
                             +  (S3 * 2**3)
                             +  (S2 * 2**2)
                             +  (S1 * 2**1)
                             +  (S0 * 2**0))
            self.check_truth_table(whenSAT, constrain, S7, [T, T, T]) # 7
            self.check_truth_table(whenSAT, constrain, S6, [T, T, F]) # 6
            self.check_truth_table(whenSAT, constrain, S5, [T, F, T]) # 5
            self.check_truth_table(whenSAT, constrain, S4, [T, F, F]) # 4
            self.check_truth_table(whenSAT, constrain, S3, [F, T, T]) # 3
            self.check_truth_table(whenSAT, constrain, S2, [F, T, F]) # 2
            self.check_truth_table(whenSAT, constrain, S1, [F, F, T]) # 1
            self.check_truth_table(whenSAT, constrain, S0, [F, F, F]) # 0

    def test_variable_numbering (self):
        expr = BooleanExpression(None)
        X = expr.add_var("X")
        Y = expr.add_var("Y")
        Z = expr.add_var("Z")
        self.assertEqual(1, X.index)
        self.assertEqual(2, Y.index)
        self.assertEqual(3, Z.index)
        # Test getting a variable that was already added.
        X = expr["X"]
        Y = expr["Y"]
        Z = expr["Z"]
        self.assertEqual(1, X.index)
        self.assertEqual(2, Y.index)
        self.assertEqual(3, Z.index)
        # Get an existing variable by number.
        self.assertIs(X, expr[1])
        self.assertIs(Y, expr[2])
        self.assertIs(Z, expr[3])

    def test_variable_naming (self):
        expr = BooleanExpression(None)
        X = expr.add_var("X") # add with name
        Y = expr.add_var() # add without name
        Z = expr["Z"] # add via get
        self.assertEqual("X", X.name)
        self.assertEqual("$2", Y.name)
        self.assertEqual("Z", Z.name)
        # str() is the name
        self.assertEqual("X", X.__str__())
        self.assertEqual("X", X.__repr__())

    def test_get_model (self):
        solver = Glucose3()
        expr = BooleanExpression(solver)
        A = expr["A"]
        B = expr["B"]
        C = expr["C"]
        D = expr["D"]
        E = expr["E"]
        TRUE(A)
        XOR(A, B)
        XOR(B, C)
        XOR(C, D)
        XOR(D, E)
        self.assertTrue(expr.solve())
        model = expr.get_model()
        self.assertEqual(5, len(model))
        self.assertEqual((A, T), model[0])
        self.assertEqual((B, F), model[1])
        self.assertEqual((C, T), model[2])
        self.assertEqual((D, F), model[3])
        self.assertEqual((E, T), model[4])

    def test_get_model_with_dont_cares (self):
        solver = Glucose3()
        expr = BooleanExpression(solver)
        A = expr["A"]
        B = expr["B"]
        C = expr["C"]
        D = expr["D"] # Don't Care
        E = expr["E"] # Don't Care
        TRUE(A)
        XOR(A, B)
        XOR(B, C)
        self.assertTrue(expr.solve())
        model = expr.get_model()
        self.assertEqual(5, len(model))
        self.assertEqual((A, T), model[0])
        self.assertEqual((B, F), model[1])
        self.assertEqual((C, T), model[2])
        self.assertEqual((D, None), model[3])
        self.assertEqual((E, None), model[4])

#
# Copyright (c) 2024 Mackenzie High. All rights reserved.
#
