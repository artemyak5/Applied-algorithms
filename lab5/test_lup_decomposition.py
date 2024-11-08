# test_lup_decomposition.py

import unittest
from lup_decomposition import Matrix, lup_decomposition, lup_solve

class TestLUPDecomposition(unittest.TestCase):

    def test_lup_decomposition(self):
        A_data = [
            [4, 3],
            [6, 3]
        ]
        L_expected = [
            [1, 0],
            [0.6667, 1]
        ]
        U_expected = [
            [6, 3],
            [0, 1]
        ]
        P_expected = [1, 0]

        L, U, P = lup_decomposition(A_data)

        # Перевірка перестановок
        self.assertEqual(P, P_expected)

        # Перевірка матриці L
        for i in range(len(L)):
            for j in range(len(L)):
                self.assertAlmostEqual(L[i][j], L_expected[i][j], places=4)

        # Перевірка матриці U
        for i in range(len(U)):
            for j in range(len(U)):
                self.assertAlmostEqual(U[i][j], U_expected[i][j], places=4)

    def test_lup_solve(self):
        A_data = [
            [2, 3],
            [5, 4]
        ]
        b = [8, 13]
        A = Matrix(A_data)
        L, U, P = lup_decomposition(A.data)
        x = lup_solve(L, U, P, b)
        x_expected = [1, 2]

        for xi, xi_expected in zip(x, x_expected):
            self.assertAlmostEqual(xi, xi_expected, places=4)

    def test_singular_matrix(self):
        A_data = [
            [1, 2],
            [2, 4]
        ]
        with self.assertRaises(ValueError):
            lup_decomposition(A_data)

unittest.main()
