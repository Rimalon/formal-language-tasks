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
        from_regex = Graph.from_regex_file(regex_path)
        print('from regex numeration dict')
        for k, v in from_regex.vertice_numbering_dictionary.items():
            print(k, ' ', v)
        print('from regex graph:')
        for label, matrix in from_regex.label_matrices.items():
            for i in range(matrix.nrows):
                for j in range(matrix.ncols):
                    print(i, ' ', j, ' ', label, ' ', matrix[i, j])
        result = from_regex.to_regex()
        print(result)
        self.assertEqual(regex, result)

    def test_from_file(self):
        graph = Graph.from_file(test_resources_path + 'graph_a_or_b.txt')
        print('from regex numeration dict')
        for k, v in graph.vertice_numbering_dictionary.items():
            print(k, ' ', v)
        print('from regex graph:')
        for label, matrix in graph.label_matrices.items():
            for i in range(matrix.nrows):
                for j in range(matrix.ncols):
                    print(i, ' ', j, ' ', label, ' ', matrix[i,j])
                    self.assertEqual((i == 0 and j == 1 and label == 'a') or (i == 0 and j == 2 and label == 'b'), matrix[i, j])


if __name__ == '__main__':
    unittest.main()
