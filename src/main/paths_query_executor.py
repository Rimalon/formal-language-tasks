from pygraphblas import Matrix, BOOL
from src.classes import Graph


def transitive_closure(matrix: Matrix) -> Matrix:
    result = matrix.dup()
    changed = True
    while changed:
        old_nvals = result.nvals
        result += result @ result
        new_nvals = result.nvals
        if old_nvals == new_nvals:
            changed = False

    return result


def execute_query(args):
    graph = Graph.from_file(args.graph)
    query = Graph.from_regex_file(args.query)
    print('graph start v:')
    print(graph.start_vertices)
    print('graph final v:')
    print(graph.final_vertices)
    print('graph:')
    for label, matrix in graph.label_matrices.items():
        print(label, ':')
        print(matrix)
    print('query start v:')
    print(query.start_vertices)
    print('query final v:')
    print(query.final_vertices)
    print('query:')
    for label, matrix in query.label_matrices.items():
        print(label, ':')
        print(matrix)

    intersection = graph & query
    intersection_matrix = Matrix.dense(BOOL, intersection.vertices_amount, intersection.vertices_amount)
    print('intersection start v:')
    print(intersection.start_vertices)
    print('intersection final v:')
    print(intersection.final_vertices)
    print('intersection result')
    for label, matrix in intersection.label_matrices.items():
        print(label, ':')
        print(matrix)
    for _, matrix in intersection.label_matrices.items():
        intersection_matrix += matrix
    print('intersection matrix')
    print(intersection_matrix)
    closure = transitive_closure(intersection_matrix)
    print('closure result')
    print(closure)

    result = Matrix.dense(BOOL, graph.vertices_amount, graph.vertices_amount)
    for i in range(closure.nrows):
        for j in range(closure.ncols):
            i_g, i_q = i // query.vertices_amount, i % query.vertices_amount
            j_g, j_q = j // query.vertices_amount, j % query.vertices_amount
            if (i_g in graph.start_states) and (i_q in query.start_states):
                if (j_g in graph.final_states) and (j_q in query.final_states):
                    result[i_g, j_g] = True
    print('result')
    print(result)
    return filter_query_result(result, None if args.fr is None else read_vertices_set_from_file(args.fr),
                               None if args.to is None else read_vertices_set_from_file(args.to))


def filter_query_result(matrix: Matrix, fr: set = None, to: set = None):
    result = Matrix.dense(BOOL, matrix.nrows, matrix.ncols)
    for i in range(matrix.nrows):
        for j in range(matrix.ncols):
            if ((fr is None or (i in fr)) and matrix[i, j]) and ((to is None or (j in to)) and matrix[i, j]):
                result[i, j] = True
    print('filter result')
    print(result)
    return result


def read_vertices_set_from_file(path):
    file = open(path)
    vertices = file.readline().split(' ')
    print(vertices)
    print(map(lambda x: int(x), vertices))
    print(set(map(lambda x: int(x), vertices)))
    file.close()
    return set(map(lambda x: int(x), vertices))
