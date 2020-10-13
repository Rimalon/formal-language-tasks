import unittest

from pyformlang.cfg import Variable

from src.classes import CNF, Graph
from src.main.CFPQ import context_free_path_querying, context_free_path_querying_tensors, \
    context_free_path_querying_matrices

test_resources_path = '/home/travis/build/Rimalon/formal-language-tasks/src/tests/resources/'
graph_path = test_resources_path + 'cfpq_graph.txt'
grammar_path = test_resources_path + 'cfpq_grammar.txt'
tensors_grammar_path = test_resources_path + 'recursive.txt'
matrices_grammar_path = test_resources_path + 'cfpq_matrices_grammar.txt'
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

    def test_context_free_path_querying_matrices(self):
        grammar = CNF.from_file(matrices_grammar_path)
        graph = Graph.from_file(graph_path)
        actual_res = context_free_path_querying_matrices(grammar, graph)
        self.assertEqual(actual_res['A'].nonzero().nvals, 3)
        self.assertEqual(actual_res['B'].nonzero().nvals, 2)
        self.assertEqual(actual_res['S'].nonzero().nvals, 6)
        self.assertEqual(actual_res['S1'].nonzero().nvals, 6)


    def test_cfpq_tensors(self):
        grammar, epsilon_set = Graph.recursive_automata_from_file(tensors_grammar_path)
        graph = Graph.from_file(graph_path)
        actual_res = context_free_path_querying_tensors(grammar, epsilon_set, graph)
        self.assertEqual(actual_res['a'].nonzero().nvals, 3)
        self.assertEqual(actual_res['b'].nonzero().nvals, 2)
        self.assertEqual(actual_res['S'].nonzero().nvals, 6)



if __name__ == '__main__':
    unittest.main()
