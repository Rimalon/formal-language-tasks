from typing import AbstractSet

from pygraphblas import Matrix, BOOL

from src.classes.CNF import CNF
from src.classes.Graph import Graph

from src.main.MatrixOperations import transitive_closure_sqr


def context_free_path_querying(grammar: CNF, graph: Graph):
    r = list()
    for production in [p for p in grammar.productions if len(p.body) == 0]:
        for vertice_num in graph.vertice_numbering_dictionary.values():
            r.append((production.head, vertice_num, vertice_num))

    for production in [p for p in grammar.productions if len(p.body) == 1]:
        if production.body[0].value in graph.label_matrices.keys():
            matrix = graph.label_matrices[production.body[0].value]
            for i, j, _ in zip(*matrix.nonzero().to_lists()):
                r.append((production.head, i, j))
    m = r.copy()
    double_productions = [p for p in grammar.productions if len(p.body) == 2]
    while len(m) != 0:
        ni, vm, um = m.pop(0)
        for nj, v1r, _ in [t for t in r if t[2] == vm]:
            for production in [p for p in double_productions if p.body[0] == nj and p.body[1] == ni
                                                                and not r.__contains__((p.head, v1r, um))]:
                m.append((production.head, v1r, um))
                r.append((production.head, v1r, um))
        for nj, _, v1r in [t for t in r if t[1] == um]:
            for production in [p for p in double_productions if p.body[0] == ni and p.body[1] == nj
                                                                and not r.__contains__((p.head, vm, v1r))]:
                m.append((production.head, vm, v1r))
                r.append((production.head, vm, v1r))
    return r


def context_free_path_querying_matrices(grammar: CNF, graph: Graph):
    t = Graph(graph.vertices_amount)
    for label, matrix in graph.label_matrices.items():
        for i, j, _ in zip(*matrix.nonzero().to_lists()):
            for production in [p for p in grammar.productions if len(p.body) == 1]:
                if production.body[0].value == label:
                    t[production.head.value][i, j] = True

    for production in [p for p in grammar.productions if len(p.body) == 0]:
        for j in range(t.vertices_amount):
            t[production.head.value][j, j] = True
    double_productions = [p for p in grammar.productions if len(p.body) == 2]
    is_changed = True
    for v in [v for v in grammar.variables if v.value not in t.label_matrices.keys()]:
        t[v.value]
    while is_changed:
        old_nvals = t.nvals()
        for label in t.label_matrices.keys():
            for production in [p for p in double_productions if label == p.head.value]:
                t[label] += t[production.body[0].value] @ t[production.body[1].value]
        is_changed = t.nvals() != old_nvals
    return t


def context_free_path_querying_tensors(rec_automata: Graph, epsilon_generate_set: AbstractSet, graph: Graph):
    m2 = graph.copy()
    for n in epsilon_generate_set:
        for j in range(m2.vertices_amount):
            m2[n][j, j] = True

    is_changed = True
    while is_changed:
        old_nvals = m2.nvals()
        intersection = rec_automata & m2
        m3 = Matrix.sparse(BOOL, intersection.vertices_amount, intersection.vertices_amount)
        for _, matrix in intersection.label_matrices.items():
            m3 += matrix
        tc3 = transitive_closure_sqr(m3)
        for i, j, _ in zip(*tc3.nonzero().to_lists()):
            if (i // graph.vertices_amount in rec_automata.start_vertices) and (j // graph.vertices_amount in rec_automata.final_vertices):
                for label, matrix in m2.label_matrices.items():
                    if label.isupper():
                        m2[label][i % m2.vertices_amount, j % m2.vertices_amount] = True
        is_changed = m2.nvals() != old_nvals
    return m2

