import argparse
import unittest
from src.main.paths_query_executor import execute_query
from src.classes import Graph

resources_path = '/home/travis/build/Rimalon/formal-language-tasks/src/tests/resources'

parser = argparse.ArgumentParser()
parser.add_argument('--graph', required=True,
                    type=str, help='path to file with graph\nfile format:\n0 a 1\n0 b 2\n1 c 2')
parser.add_argument('--queries', required=True,
                    type=str, help='path to file with query\nfile format: regex in first line')
parser.add_argument('--fr', required=False, default=None,
                    type=str, help='path to file with start vertices\nfile format:\n0 1 2')
parser.add_argument('--to', required=False, default=None,
                    type=str, help='path to file with end vertices\nfile format:\n0 1 2')


class PQECase(unittest.TestCase):
    def test_graph_regex_abc_from0_to2(self):
        args = parser.parse_args(args=('--graph ' + resources_path + '/graph.txt ' +
                                       '--queries ' + resources_path + '/regex_abc.txt ' +
                                       '--fr ' + resources_path + '/vertices_0.txt ' +
                                       '--to ' + resources_path + '/vertices_2.txt').split())
        graph = Graph.from_file(args.graph)
        query = Graph.from_regex_file(args.queries)
        automata, reachable_vertices_matrix = execute_query(args, graph, query)
        self.assertEqual(automata['a'].nonzero().nvals, 1)
        self.assertEqual(automata['b'].nonzero().nvals, 2)
        self.assertEqual(automata['c'].nonzero().nvals, 2)
        excepted_reachable_vertices = {(0, 2)}
        for i, j, _ in zip(*reachable_vertices_matrix.nonzero().to_lists()):
            self.assertEqual(reachable_vertices_matrix[i, j], (i, j) in excepted_reachable_vertices)

    def test_graph_regex_abc_from2_to2(self):
        args = parser.parse_args(args=('--graph ' + resources_path + '/graph.txt ' +
                                       '--queries ' + resources_path + '/regex_abc.txt ' +
                                       '--fr ' + resources_path + '/vertices_2.txt ' +
                                       '--to ' + resources_path + '/vertices_2.txt').split())
        graph = Graph.from_file(args.graph)
        query = Graph.from_regex_file(args.queries)
        automata, reachable_vertices_matrix = execute_query(args, graph, query)
        excepted_reachable_vertices = {}
        for i, j, _ in zip(*reachable_vertices_matrix.nonzero().to_lists()):
            self.assertEqual(reachable_vertices_matrix[i, j], (i, j) in excepted_reachable_vertices)

    def test_graph_regex_abc_to2(self):
        args = parser.parse_args(args=('--graph ' + resources_path + '/graph.txt ' +
                                       '--queries ' + resources_path + '/regex_abc.txt ' +
                                       '--to ' + resources_path + '/vertices_2.txt').split())
        graph = Graph.from_file(args.graph)
        query = Graph.from_regex_file(args.queries)
        automata, reachable_vertices_matrix = execute_query(args, graph, query)
        excepted_reachable_vertices = {(0, 2), (1, 2)}
        for i, j, _ in zip(*reachable_vertices_matrix.nonzero().to_lists()):
            self.assertEqual(reachable_vertices_matrix[i, j], (i, j) in excepted_reachable_vertices)

    def test_graph_regex_abc_from0(self):
        args = parser.parse_args(args=('--graph ' + resources_path + '/graph.txt ' +
                                       '--queries ' + resources_path + '/regex_abc.txt ' +
                                       '--fr ' + resources_path + '/vertices_0.txt').split())
        graph = Graph.from_file(args.graph)
        query = Graph.from_regex_file(args.queries)
        automata, reachable_vertices_matrix = execute_query(args, graph, query)
        excepted_reachable_vertices = {(0, 1), (0, 2), (0, 3)}
        for i, j, _ in zip(*reachable_vertices_matrix.nonzero().to_lists()):
            self.assertEqual(reachable_vertices_matrix[i, j], (i, j) in excepted_reachable_vertices)

    def test_graph_regex_abc(self):
        args = parser.parse_args(args=('--graph ' + resources_path + '/graph.txt ' +
                                       '--queries ' + resources_path + '/regex_abc.txt').split())
        graph = Graph.from_file(args.graph)
        query = Graph.from_regex_file(args.queries)
        automata, reachable_vertices_matrix = execute_query(args, graph, query)
        excepted_reachable_vertices = {(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)}
        for i, j, _ in zip(*reachable_vertices_matrix.nonzero().to_lists()):
            self.assertEqual(reachable_vertices_matrix[i, j], (i, j) in excepted_reachable_vertices)


if __name__ == '__main__':
    unittest.main()
