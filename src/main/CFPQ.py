from src.classes import Graph, CNF


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
