import unittest

from pyformlang.cfg import Terminal, Variable, CFG

from src.classes.CNF import CNF
from src.main.CYK import cyk
from syntactic_analyzer import check_syntax

project_path = '/home/travis/build/Rimalon/formal-language-tasks/'
resources_path = project_path + 'src/tests/resources/'
syntax_grammar_path = project_path + 'syntax_grammar.txt'


class SyntaxCheckTestCase(unittest.TestCase):
    def test_correct_syntax_success(self):
        self.assertTrue(check_syntax(resources_path + 'script_correct_example.txt'))

    def test_incorrect_syntax_fail(self):
        self.assertFalse(check_syntax(resources_path + 'script_incorrect_example.txt'))

    def test_correct_syntax(self):
        file = open(resources_path + 'syntax_expressions_data.txt')
        expressions = file.read().split('\n')
        file.close()
        file = open(syntax_grammar_path)
        syntax_grammar_text = file.read()
        file.close()
        for expr in expressions:
            test_res, expr_type, expr_value = expr.split(' ', 2)
            syntax_grammar = CNF(CFG.from_text(syntax_grammar_text, Variable(expr_type)), True)
            self.assertEqual(test_res, str(cyk(prepare_word(expr_value), syntax_grammar)), expr)


def prepare_word(word: str): return list(map(lambda c: Terminal(c), list(word.replace('\n', '').replace(' ', '#'))))


if __name__ == '__main__':
    unittest.main()
