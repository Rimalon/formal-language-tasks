import unittest

from src.classes import Graph

test_resources_path = '/home/travis/build/Rimalon/formal-language-tasks/src/tests/resources/'


class GraphTestCase(unittest.TestCase):
    def test_from_file(self):
        graph = Graph.from_file(test_resources_path + 'graph.txt')
        self.assertTrue(graph['a'][0, 1])
        self.assertTrue(graph['b'][1, 2])
        self.assertTrue(graph['c'][2, 3])
        self.assertTrue(graph['c'][0, 1])
        self.assertTrue(graph['b'][1, 3])
        self.assertFalse(graph['a'][0, 2])
        self.assertFalse(graph['b'][0, 1])
        self.assertFalse(graph['c'][0, 3])


if __name__ == '__main__':
    unittest.main()
