import argparse
from src.main.paths_query_executor import execute_query
from pygraphblas import lib

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--graph', required=True,
                        type=str, help='path to file with graph\nfile format:\n0 a 1\n0 b 2\n1 c 2')
    parser.add_argument('--query', required=True,
                        type=str, help='path to file with query\nfile format: regex in first line')
    parser.add_argument('--fr', required=False, default=None,
                        type=str, help='path to file with start vertices\nfile format:\n0 1 2')
    parser.add_argument('--to', required=False, default=None,
                        type=str, help='path to file with end vertices\nfile format:\n0 1 2')
    args = parser.parse_args()
    intersection, reachable_vertices = execute_query(args)
    print('intersection statistic:')
    for label, matrix in intersection.label_matrices.items():
        print('label: ', label, ': ', matrix.select(lib.GxB_NONZERO).nvals, ' - vertices amount')
    print('reachable vertices')
    for i in range(reachable_vertices.nrows):
        for j in range(reachable_vertices.ncols):
            if reachable_vertices[i, j]:
                print(j, ' reachable from ', i)
