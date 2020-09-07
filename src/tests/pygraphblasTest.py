import unittest
from pygraphblas import Matrix, INT64

first_matrix = Matrix.from_lists(
    [0, 0, 0, 1, 1, 1, 2, 2, 2],
    [0, 1, 2, 0, 1, 2, 0, 1, 2],
    [1, 2, 3, -4, 5, 6, 7, 8, -9],
    typ=INT64,
)
second_matrix = Matrix.from_lists(
    [0, 0, 0, 1, 1, 1, 2, 2, 2],
    [0, 1, 2, 0, 1, 2, 0, 1, 2],
    [10, -1, 8, -5, 2, 3, -4, 6, -2],
    typ=INT64,
)
result_matrix = Matrix.from_lists(
    [0, 0, 0, 1, 1, 1, 2, 2, 2],
    [0, 1, 2, 0, 1, 2, 0, 1, 2],
    [-12, 21, 8, -89, 50, -29, 66, -45, 98],
    typ=INT64,
)

zero_matrix = Matrix.from_lists(
    [0, 0, 0, 1, 1, 1, 2, 2, 2],
    [0, 1, 2, 0, 1, 2, 0, 1, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    typ=INT64,
)
identity_matrix = Matrix.from_lists(
    [0, 0, 0, 1, 1, 1, 2, 2, 2],
    [0, 1, 2, 0, 1, 2, 0, 1, 2],
    [1, 0, 0, 0, 1, 0, 0, 0, 1],
    typ=INT64,
)


class PygraphblasTestCase(unittest.TestCase):
    def test_non_zero_matrix_product(self):
        for line in first_matrix & second_matrix:
            print(line)
        self.assertTrue(result_matrix.iseq(first_matrix & second_matrix))

    def test_zero_matrix_product(self):
        self.assertTrue(zero_matrix.iseq(first_matrix & zero_matrix))

    def test_identity_matrix_product(self):
        for line in first_matrix & identity_matrix:
            print(line)
        self.assertTrue(first_matrix.iseq(first_matrix & identity_matrix))


if __name__ == '__main__':
    unittest.main()
