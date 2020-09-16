import unittest

from pyformlang.regular_expression import Regex
from src.classes import Graph

test_resources_path = '/home/travis/build/Rimalon/formal-language-tasks/src/tests/resources/'


class GraphTestCase(unittest.TestCase):
    def test_from_regex(self):
        graph = Graph.from_regex_file(test_resources_path + 'regex_a_or_b.txt')
        for label, matrix in graph.label_matrices.items():
            for i in range(matrix.nrows):
                for j in range(matrix.ncols):
                    print(i, ' ', j, ' ', label, ' ', matrix[i, j])
                    #self.assertEqual((i == 0 and j == 1 and label == 'a') or (i == 0 and j == 2 and label == 'b'), matrix[i, j])

    def test_from_file(self):
        graph = Graph.from_file(test_resources_path + 'graph_a_or_b.txt')
        for label, matrix in graph.label_matrices.items():
            for i in range(matrix.nrows):
                for j in range(matrix.ncols):
                    print(i, ' ', j, ' ', label, ' ', matrix[i, j])
                    #self.assertEqual((i == 0 and j == 1 and label == 'b') or (i == 0 and j == 2 and label == 'a'), matrix[i, j])


if __name__ == '__main__':
    unittest.main()
