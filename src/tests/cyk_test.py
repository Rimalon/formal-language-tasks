import unittest

from pyformlang.cfg import Terminal, Variable

from src.classes import CNF
from src.main.CYK import cyk

aSbS = '/home/travis/build/Rimalon/formal-language-tasks/src/tests/resources/grammar_aSbS_or_epsilon.txt'
aNbN = '/home/travis/build/Rimalon/formal-language-tasks/src/tests/resources/grammar_a^nb^n.txt'
task_1_grammar = '/home/travis/build/Rimalon/formal-language-tasks/src/tests/resources/task_4_3_1_grammar_example.txt'
a = Terminal('a')
b = Terminal('b')
mult = Terminal('*')
plus = Terminal('+')
n = Terminal('n')
open = Terminal('(')
close = Terminal(')')

class CykTestCase(unittest.TestCase):
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
        grammar = CNF.from_file(aSbS, is_reduced=True)
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
        grammar = CNF.from_file(aNbN, is_reduced=True)
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

    def test_task_4_3_1(self):
        grammar = CNF.from_file(task_1_grammar, Variable('E'))
        self.assertFalse(cyk([], grammar))
        self.assertTrue(cyk([open, n, plus, n, close, mult, n], grammar))
        self.assertTrue(cyk([n, plus, n, mult, n], grammar))
        self.assertTrue(cyk([n, plus, n, plus, n, plus, n], grammar))
        self.assertTrue(cyk([n, plus, open, n, mult, n, close, plus, n], grammar))
        self.assertFalse(cyk([n, plus, n, mult, n, close, plus, n], grammar))
        self.assertFalse(cyk([n, plus, open, n, mult, n, close, n], grammar))
        self.assertFalse(cyk([n, plus, open, n, mult, close, plus, n], grammar))
        self.assertFalse(cyk([plus, open, n, mult, n, close, plus, n], grammar))


if __name__ == '__main__':
    unittest.main()
