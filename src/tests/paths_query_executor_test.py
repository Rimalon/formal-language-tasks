import unittest
from src.main.paths_query_executor import execute_query

resources_path = '/home/travis/build/Rimalon/formal-language-tasks/src/tests/resources/'


class PQECase(unittest.TestCase):
    def test_graph_regex_abc_from0_to2(self):
        automata, reachable_vertices_matrix = execute_query(args={'graph': resources_path + '/graph.txt',
                                                                  'query': resources_path + '/regex_abc.txt',
                                                                  'fr': resources_path + '/vertices_0.txt',
                                                                  'to': resources_path + '/vertices_2.txt'})
        self.assertEqual(automata['a'].nonzero().nvals, 1)
        self.assertEqual(automata['b'].nonzero().nvals, 2)
        self.assertEqual(automata['c'].nonzero().nvals, 2)
        excepted_reachable_vertices = {(0, 2)}
        for i, j, _ in zip(reachable_vertices_matrix.nonzero().to_lists()):
            self.assertTrue(i, j in excepted_reachable_vertices)

    def test_graph_regex_abc_from2_to2(self):
        automata, reachable_vertices_matrix = execute_query(args={'graph': resources_path + '/graph.txt',
                                                                  'query': resources_path + '/regex_abc.txt',
                                                                  'fr': resources_path + '/vertices_2.txt',
                                                                  'to': resources_path + '/vertices_2.txt'})
        excepted_reachable_vertices = {}
        for i, j, _ in zip(reachable_vertices_matrix.nonzero().to_lists()):
            self.assertTrue((i, j) in excepted_reachable_vertices)

    def test_graph_regex_abc_to2(self):
        automata, reachable_vertices_matrix = execute_query(args={'graph': resources_path + '/graph.txt',
                                                                  'query': resources_path + '/regex_abc.txt',
                                                                  'to': resources_path + '/vertices_2.txt'})
        excepted_reachable_vertices = {(0, 2), (1, 2)}
        for i, j, _ in zip(reachable_vertices_matrix.nonzero().to_lists()):
            self.assertTrue(i, j in excepted_reachable_vertices)

    def test_graph_regex_abc_from0(self):
        automata, reachable_vertices_matrix = execute_query(args={'graph': resources_path + '/graph.txt',
                                                                  'query': resources_path + '/regex_abc.txt',
                                                                  'fr': resources_path + '/vertices_2.txt'})
        excepted_reachable_vertices = {(0, 1), (0, 2), (0, 3)}
        for i, j, _ in zip(reachable_vertices_matrix.nonzero().to_lists()):
            self.assertTrue(i, j in excepted_reachable_vertices)

    def test_graph_regex_abc(self):
        automata, reachable_vertices_matrix = execute_query(args={'graph': resources_path + '/graph.txt',
                                                                  'query': resources_path + '/regex_abc.txt'})
        excepted_reachable_vertices = {(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)}
        for i, j, _ in zip(reachable_vertices_matrix.nonzero().to_lists()):
            self.assertTrue(i, j in excepted_reachable_vertices)


if __name__ == '__main__':
    unittest.main()
