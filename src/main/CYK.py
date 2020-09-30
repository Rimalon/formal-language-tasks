from typing import List

from pyformlang.cfg import Terminal
import numpy as np
from src.classes import CNF


def cyk(word: List[Terminal], cnf: CNF):
    n = len(word)
    if n == 0:
        return cnf.generate_epsilon()
    numbering_dict = dict()
    for index, symbol in enumerate(cnf.variables):
        numbering_dict[symbol] = index
    m = np.zeros((n, n, len(cnf.variables)), bool)
    for s in range(n):
        for production in cnf.productions:
            if len(production.body) == 1 and production.body[0] == word[s]:
                m[0, s, numbering_dict[production.head]] = True
    for l in range(1, n):
        for s in range(n - l):
            for p in range(l):
                for production in cnf.productions:
                    if len(production.body) == 2 and m[p, s, numbering_dict[production.body[0]]] and m[l - p - 1, s + p + 1, numbering_dict[production.body[1]]]:
                        m[l, s, numbering_dict[production.head]] = True
    return m[n - 1, 0, numbering_dict[cnf.start_symbol]]
