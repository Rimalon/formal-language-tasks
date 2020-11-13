import argparse
import os

from pyformlang.cfg import Terminal, CFG, Variable

from src.classes.CNF import CNF
from src.main.CYK import cyk

syntax_grammar_path_default = os.path.join(os.path.dirname(__file__), 'syntax_grammar.txt')


def check_syntax(script_path: str, syntax_grammar_path: str = syntax_grammar_path_default):
    file = open(script_path)
    script_content = prepare_script(file.read())
    file.close()
    file = open(syntax_grammar_path)
    syntax_grammar_text = file.read()
    file.close()
    syntax_grammar = CNF(CFG.from_text(syntax_grammar_text, Variable('Script')), True)
    return cyk(script_content, syntax_grammar)


def prepare_script(script: str): return list(map(lambda c: Terminal(c), list(script.replace('\n', '').replace(' ', '#'))))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--script', required=True,
                        type=str, help='path to file with script.\nthe file format depends on your syntax')
    parser.add_argument('--syntax', required=False,
                        type=str, help='path to file with syntax.\nfile format(pyformlang.cfg format):\nString -> Char String\nChar -> a | b\n')
    args = parser.parse_args()
    if args.syntax is None:
        result = check_syntax(args.script)
    else:
        result = check_syntax(args.script, args.syntax)
    if result:
        print('Correct script')
    else:
        print('Incorrect script')

