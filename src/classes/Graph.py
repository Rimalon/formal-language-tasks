from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State, Symbol
from pygraphblas import Matrix, BOOL
from pyformlang.regular_expression import Regex


class Graph:
    def __init__(self, vertices_amount=0):
        self.label_matrices = dict()
        self.vertice_numbering_dictionary = dict()
        self.vertices_amount = vertices_amount
        self.start_vertices = set(range(vertices_amount))
        self.final_vertices = set(range(vertices_amount))

    def __getitem__(self, item) -> Matrix:
        if item not in self.label_matrices.keys():
            self.label_matrices[item] = Matrix.sparse(BOOL, self.vertices_amount, self.vertices_amount)
        return self.label_matrices[item]

    def __and__(self, other):
        return self.get_intersection(other)

    def get_intersection(self, other: "Graph"):
        result = Graph(self.vertices_amount * other.vertices_amount)
        for i in self.start_vertices:
            for j in other.start_vertices:
                result.start_vertices.add(i * other.vertices_amount + j)

        for i in self.final_vertices:
            for j in other.final_vertices:
                result.final_vertices.add(i * other.vertices_amount + j)

        for label in self.label_matrices.keys():
            result.label_matrices[label] = self[label].kronecker(other[label])

        return result

    def to_dfa(self):
        result = DeterministicFiniteAutomaton(states=set(self.vertice_numbering_dictionary.keys()),
                                              start_state=State(self.start_vertices.pop()),
                                              final_states=set(map(lambda x: State(x), self.final_vertices)))
        for label, matrix in self.label_matrices.items():
            for i in range(matrix.nrows):
                for j in range(matrix.ncols):
                    if self.label_matrices[label][i, j]:
                        result.add_transition(State(i), Symbol(label), State(j))
        return result

    def to_regex(self):
        return self.to_dfa().to_regex()


def from_file(path: str):
    file = open(path)
    transitions = file.read().split('\n')
    transitions = filter(lambda x: x != '', transitions)
    file.close()
    result = Graph()
    i = 0
    for t in transitions:
        fr, label, to = t.split(' ')
        if fr not in result.vertice_numbering_dictionary.keys():
            result.vertice_numbering_dictionary[fr] = i
            i += 1

        if to not in result.vertice_numbering_dictionary.keys():
            result.vertice_numbering_dictionary[to] = i
            i += 1
    result.vertices_amount = len(result.vertice_numbering_dictionary)
    result.start_vertices = set(range(result.vertices_amount))
    result.final_vertices = set(range(result.vertices_amount))
    for t in transitions:
        fr, label, to = t.split(' ')
        result[label][result.vertice_numbering_dictionary[fr], result.vertice_numbering_dictionary[to]] = True

    return result


def from_regex_file(path: str):
    file = open(path)
    regex = Regex(file.readline())
    file.close()
    dfa: DeterministicFiniteAutomaton = regex.to_epsilon_nfa().to_deterministic().minimize()
    return from_dfa(dfa)


def from_dfa(dfa: DeterministicFiniteAutomaton):
    result = Graph()
    i = 0
    for s in dfa.states:
        if s not in result.vertice_numbering_dictionary.keys():
            result.vertice_numbering_dictionary[s] = i
            i += 1

    result.vertices_amount = len(result.vertice_numbering_dictionary)
    for fr, label, to in dfa._transition_function.get_edges():
        result[label][result.vertice_numbering_dictionary[fr], result.vertice_numbering_dictionary[to]] = True

    for fs in dfa.final_states:
        result.final_vertices.add(result.vertice_numbering_dictionary[fs])

    result.start_vertices.add(result.vertice_numbering_dictionary[dfa.start_state])
    return result
