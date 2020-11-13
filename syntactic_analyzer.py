from pyformlang.cfg import Terminal, CFG, Variable

from src.classes.CNF import CNF
from src.main.CYK import cyk

def check_syntax(syntax_grammar_path:str, script_path: str):
    file = open(script_path)
    script_content = prepare_script(file.read())
    file.close()
    file = open(syntax_grammar_path)
    syntax_grammar_text = file.read()
    file.close()
    syntax_grammar = CNF(CFG.from_text(syntax_grammar_text, Variable('Script')), True)
    return cyk(script_content, syntax_grammar)


def prepare_script(script: str): return list(map(lambda c: Terminal(c), list(script.replace('\n', '').replace(' ', '#'))))
