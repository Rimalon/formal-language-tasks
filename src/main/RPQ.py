from pygraphblas import Matrix, BOOL

from src.main.MatrixOperations import transitive_closure_adj, transitive_closure_sqr

"""Regular Path Querying.

This program calculates the reachable vertices in the graph for the corresponding query.

  Typical usage example:
  args = parser.parse_args()
  graph = Graph.from_file(path_to_graph)
  query = Graph.from_regex_file(path_to_query)
  intersection, result = execute_query(args, graph, query)
  
"""


def execute_query(args, graph, query):
    """Finds reachable vertices in a graph for a query.

        Args:
            args: Parsed command line arguments that can contain fr: str (path to a file that contains many start vertices),
                  to: str (path to a file that contains many end vertices),
                  type: str (transitive closure type: Used 'adj' for multiplication by an adjacency matrix or
                        otherwise squaring is used
            graph: src.classes.Graph containing vertices to search
            query: src.classes.Graph containing path constraints

        Returns:
            A pair consisting of the intersection of a graph and a query and a matrix of reachable vertices.

    """
    intersection = graph & query
    intersection_matrix = Matrix.sparse(BOOL, intersection.vertices_amount, intersection.vertices_amount)

    for _, matrix in intersection.label_matrices.items():
        intersection_matrix += matrix
    if args.type == 'adj':
        print("adj closure:")
        closure = transitive_closure_adj(intersection_matrix)
    else:
        print("sqr closure:")
        closure = transitive_closure_sqr(intersection_matrix)

    result = Matrix.sparse(BOOL, graph.vertices_amount, graph.vertices_amount)
    for i, j, _ in zip(*closure.nonzero().to_lists()):
        if (i in intersection.start_vertices) and (j in intersection.final_vertices):
            result[i // query.vertices_amount, j // query.vertices_amount] = True
    return intersection, filter_query_result(result, None if args.fr is None else read_vertices_set_from_file(args.fr),
                                             None if args.to is None else read_vertices_set_from_file(args.to))


def filter_query_result(matrix: Matrix, fr: set = None, to: set = None) -> Matrix:
    result = Matrix.sparse(BOOL, matrix.nrows, matrix.ncols)
    for i, j, _ in zip(*matrix.nonzero().to_lists()):
        if ((fr is None or (i in fr)) and matrix[i, j]) and ((to is None or (j in to)) and matrix[i, j]):
            result[i, j] = True
    return result


def read_vertices_set_from_file(path):
    file = open(path)
    vertices = file.readline().split(' ')
    file.close()
    return set(map(lambda x: int(x), vertices))
