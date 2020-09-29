import unittest

from pyformlang.cfg import Variable

from src.classes import CNF, Graph
from src.main.CFPQ import context_free_path_querying

graph_path = '/home/travis/build/Rimalon/formal-language-tasks/src/tests/resources/cfpq_graph.txt'
grammar_path = '/home/travis/build/Rimalon/formal-language-tasks/src/tests/resources/cfpq_grammar.txt'
S = Variable('S')
A = Variable('A')
B = Variable('B')
S1 = Variable('S1')
expected_res = [(A, 0, 1), (A, 1, 2), (A, 2, 0), (B, 2, 3), (B, 3, 2), (S, 1, 3), (S1, 1, 2), (S, 0, 2), (S1, 0, 3),
                (S, 2, 3), (S1, 2, 2), (S, 1, 2), (S1, 1, 3), (S, 0, 3), (S1, 0, 2), (S, 2, 2), (S1, 2, 3)]


class CFPQTestCase(unittest.TestCase):
    def test_cfpq(self):
        grammar = CNF.from_file(grammar_path, is_reduced=True)
        graph = Graph.from_file(graph_path)
        actual_res = context_free_path_querying(grammar, graph)
        self.assertEqual(len(actual_res), len(expected_res))
        for tuple in expected_res:
            self.assertTrue(actual_res.__contains__(tuple))


if __name__ == '__main__':
    unittest.main()
