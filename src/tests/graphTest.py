import unittest

from pyformlang.regular_expression import Regex
from src.classes import Graph

test_resources_path = '/home/travis/build/Rimalon/formal-language-tasks/src/tests/resources/'


class GraphTestCase(unittest.TestCase):
    def test_from_regex_to_regex(self):
        regex_path = test_resources_path + 'regex_a_or_b.txt'
        file = open(regex_path)
        regex = Regex(file.readline())
        file.close()
        result = Graph.from_regex_file(regex_path).to_regex()
        self.assertEqual(regex, result)

    def test_from_file(self):
        graph = Graph.from_file(test_resources_path + 'graph_a_or_b.txt')
        for label, matrix in graph.label_matrices.items():
            for i in range(len(matrix.rows)):
                for j in range(len(matrix.cols)):
                    self.assertEqual((i == 0 & j == 1 & label == 'a') | (i == 0 & j == 2 & label == 'b'), matrix[i, j])


if __name__ == '__main__':
    unittest.main()
