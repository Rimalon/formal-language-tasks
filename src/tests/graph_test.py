import unittest

from src.classes import Graph

test_resources_path = '/home/travis/build/Rimalon/formal-language-tasks/src/tests/resources/'


class GraphTestCase(unittest.TestCase):
    def test_from_file(self):
        graph = Graph.from_file(test_resources_path + 'graph.txt')
        self.assertEqual(graph['a'].nonzero().nvals, 1)
        self.assertEqual(graph['b'].nonzero().nvals, 2)
        self.assertEqual(graph['c'].nonzero().nvals, 2)
        self.assertTrue(graph['a'][0, 1])
        self.assertTrue(graph['b'][1, 2])
        self.assertTrue(graph['c'][2, 3])
        self.assertTrue(graph['c'][0, 1])
        self.assertTrue(graph['b'][1, 3])

    def test_recursive_automata_from_file(self):
        graph = Graph.recursive_automata_from_file(test_resources_path + 'recursive.txt')
        self.assertEqual(graph['a'].nonzero().nvals, 1)
        self.assertEqual(graph['b'].nonzero().nvals, 2)
        self.assertEqual(graph['S'].nonzero().nvals, 1)


if __name__ == '__main__':
    unittest.main()
