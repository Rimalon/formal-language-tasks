import argparse
from src.main.paths_query_executor import execute_query

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
    query_result = execute_query(args)
    closure, reachable_vertices = query_result
    print('closure statistic:')
    for label, matrix in closure:
        print('label: ', label, ': ', matrix.nvals, ' - vertices amount')
    print('reachable vertices')
    for i in range(query_result.nrows):
        for j in range(query_result.ncols):
            if query_result[i, j]:
                print(j, ' reachable from ', i)
