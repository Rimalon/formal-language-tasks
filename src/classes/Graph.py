from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State
from pygraphblas import Matrix, BOOL
from pyformlang.regular_expression import Regex


class Graph:
    def __init__(self):
        self.label_matrices = dict()
        self.vertice_numbering_dictionary = dict()
        self.start_vertice = None
        self.final_vertices = set()

    def to_dfa(self):
        result = DeterministicFiniteAutomaton(states=set(self.vertice_numbering_dictionary.keys()),
                                              start_state=State(self.start_vertice),
                                              final_states=set(map(lambda x: State(x), self.final_vertices)))
        for label, matrix in self.label_matrices.items():
            for i in range(len(matrix.rows)):
                for j in range(len(matrix.cols)):
                    if self.label_matrices[label][i, j]:
                        result.add_transition(State(i), label, State(j))
        return result

    def to_regex(self):
        return self.to_dfa().to_regex()


def from_file(path: str):
    file = open(path)
    transitions = file.read().split('\n')
    file.close()
    result = Graph()
    for t in transitions:
        fr, label, to = t.split(' ')
        i = 0
        if fr not in result.vertice_numbering_dictionary.keys():
            result.vertice_numbering_dictionary[fr] = i
            i += 1

        if to not in result.vertice_numbering_dictionary.keys():
            result.vertice_numbering_dictionary[to] = i
            i += 1

    for t in transitions:
        fr, label, to = t.split(' ')
        if label not in result.label_matrices.keys():
            result.label_matrices[label] = Matrix.sparse(BOOL, len(result.vertice_numbering_dictionary),
                                                         len(result.vertice_numbering_dictionary))
        result.label_matrices[label][int(fr), int(to)] = True

    return result


def from_regex_file(path: str):
    file = open(path)
    regex = Regex(file.readline())
    file.close()
    dfa: DeterministicFiniteAutomaton = regex.to_epsilon_nfa().to_deterministic().minimize()
    return cls.from_dfa(dfa)


def from_dfa(dfa: DeterministicFiniteAutomaton):
    result = Graph()
    for s in dfa.states:
        i = 0
        if s not in result.vertice_numbering_dictionary.keys():
            result.vertice_numbering_dictionary[s] = i
            i += 1

    for fr, label, to in dfa._transition_function.get_edges():
        if label not in result.label_matrices.keys():
            result.label_matrices[label] = Matrix.sparse(BOOL, len(result.vertice_numbering_dictionary),
                                                         len(result.vertice_numbering_dictionary))
        result.label_matrices[label][int(fr), int(to)] = True

    for fs in dfa.final_states:
        result.final_vertices.add(result.vertice_numbering_dictionary[fs])

    result.start_vertice = result.vertice_numbering_dictionary[dfa.start_state]
    return result
