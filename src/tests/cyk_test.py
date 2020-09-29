import unittest

from pyformlang.cfg import Terminal

from src.classes import CNF
from src.main.CYK import cyk

aSbS = '/home/travis/build/Rimalon/formal-language-tasks/src/tests/resources/grammar_aSbS_or_epsilon.txt'
aNbN = '/home/travis/build/Rimalon/formal-language-tasks/src/tests/resources/grammar_a^nb^n.txt'
a = Terminal('a')
b = Terminal('b')


class MyTestCase(unittest.TestCase):
    def test_aSbS_cyk(self):
        grammar = CNF.from_file(aSbS)
        self.assertTrue(cyk([], grammar))
        self.assertTrue(cyk([a, b], grammar))
        self.assertTrue(cyk([a, a, b, b], grammar))
        self.assertTrue(cyk([a, a, a, b, b, b], grammar))
        self.assertTrue(cyk([a, a, a, a, a, b, b, b, b, b], grammar))
        self.assertTrue(cyk([a, b, a, b], grammar))
        self.assertFalse(cyk([a, b, a], grammar))
        self.assertFalse(cyk([a, a, a, a, b], grammar))
        self.assertFalse(cyk([a, b, b, b, b], grammar))
        self.assertFalse(cyk([a, a, a, a, a], grammar))
        self.assertFalse(cyk([b, b, b, b, b], grammar))

    def test_aSbS_cyk_reduced(self):
        grammar = CNF.from_file(aSbS, True)
        self.assertTrue(cyk([], grammar))
        self.assertTrue(cyk([a, b], grammar))
        self.assertTrue(cyk([a, a, b, b], grammar))
        self.assertTrue(cyk([a, a, a, b, b, b], grammar))
        self.assertTrue(cyk([a, a, a, a, a, b, b, b, b, b], grammar))
        self.assertTrue(cyk([a, b, a, b], grammar))
        self.assertFalse(cyk([a, b, a], grammar))
        self.assertFalse(cyk([a, a, a, a, b], grammar))
        self.assertFalse(cyk([a, b, b, b, b], grammar))
        self.assertFalse(cyk([a, a, a, a, a], grammar))
        self.assertFalse(cyk([b, b, b, b, b], grammar))

    def test_aNbN_cyk(self):
        grammar = CNF.from_file(aNbN)
        self.assertTrue(cyk([], grammar))
        self.assertTrue(cyk([a, b], grammar))
        self.assertTrue(cyk([a, a, b, b], grammar))
        self.assertTrue(cyk([a, a, a, a, a, b, b, b, b, b], grammar))
        self.assertFalse(cyk([a, b, a, b], grammar))
        self.assertFalse(cyk([a, b, a], grammar))
        self.assertFalse(cyk([a, a, a, a, b], grammar))
        self.assertFalse(cyk([a, b, b, b, b], grammar))
        self.assertFalse(cyk([a, a, a, a, a], grammar))
        self.assertFalse(cyk([b, b, b, b, b], grammar))


    def test_aNbN_cyk_reduced(self):
        grammar = CNF.from_file(aNbN, True)
        self.assertTrue(cyk([], grammar))
        self.assertTrue(cyk([a, b], grammar))
        self.assertTrue(cyk([a, a, b, b], grammar))
        self.assertTrue(cyk([a, a, a, a, a, b, b, b, b, b], grammar))
        self.assertFalse(cyk([a, b, a, b], grammar))
        self.assertFalse(cyk([a, b, a], grammar))
        self.assertFalse(cyk([a, a, a, a, b], grammar))
        self.assertFalse(cyk([a, b, b, b, b], grammar))
        self.assertFalse(cyk([a, a, a, a, a], grammar))
        self.assertFalse(cyk([b, b, b, b, b], grammar))


if __name__ == '__main__':
    unittest.main()
