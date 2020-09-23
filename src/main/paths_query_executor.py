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

    intersection = graph & query
    intersection_matrix = Matrix.sparse(BOOL, intersection.vertices_amount, intersection.vertices_amount)

    for _, matrix in intersection.label_matrices.items():
        intersection_matrix += matrix

    closure = transitive_closure(intersection_matrix)

    result = Matrix.sparse(BOOL, graph.vertices_amount, graph.vertices_amount)
    for i, j, _ in zip(*closure.select(lib.GxB_NONZERO).to_lists()):
        if (i in intersection.start_vertices) and (j in intersection.final_vertices) and (closure[i, j]):
            result[i // query.vertices_amount, j // query.vertices_amount] = True
    return intersection, filter_query_result(result, None if args.fr is None else read_vertices_set_from_file(args.fr),
                               None if args.to is None else read_vertices_set_from_file(args.to))


def filter_query_result(matrix: Matrix, fr: set = None, to: set = None) -> Matrix:
    result = Matrix.sparse(BOOL, matrix.nrows, matrix.ncols)
    for i, j, _ in zip(*matrix.select(lib.GxB_NONZERO).to_lists()):
        if ((fr is None or (i in fr)) and matrix[i, j]) and ((to is None or (j in to)) and matrix[i, j]):
            result[i, j] = True
    return result


def read_vertices_set_from_file(path):
    file = open(path)
    vertices = file.readline().split(' ')
    file.close()
    return set(map(lambda x: int(x), vertices))
