from pygraphblas import Matrix, BOOL
from src.classes import Graph


def transitive_closure(matrix: Matrix) -> Matrix:
    result = matrix.dup()
    changed = True
    while changed:
        old_nvals = result.nvals
        result += result @ result
        new_nvals = result.nvals
        if old_nvals != new_nvals:
            changed = False

    return result


def execute_query(args):
    graph = Graph.from_file(args.graph)
    query = Graph.from_regex_file(args.query)

    intersection = graph & query
    intersection_matrix = Matrix.dense(BOOL, intersection.vertices_amount, intersection.vertices_amount)
    print('intersection result')
    for label, matrix in intersection.label_matrices:
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
            if (i in intersection.start_vertices) and (j in intersection.final_vertices):
                result[i // graph.vertices_amount, j % graph.vertices_amount] = True
    print('result')
    print(result)
    return filter_query_result(result, args.fr, args.to)


def filter_query_result(matrix: Matrix, fr: set = None, to: set = None):
    result = Matrix.dense(BOOL, matrix.nrows, matrix.ncols)
    for i in range(matrix.nrows):
        for j in range(matrix.ncols):
            if (fr is None or (i in fr)) and (to is None or (j in to)):
                result[i, j] = True
    print('filter result')
    print(result)
    return result


def read_vertices_set_from_file(path):
    file = open(path)
    vertices = file.readline().split(' ')
    file.close()
    return set(map(lambda x: int(x), vertices))
