import argparse
import datetime

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
    start_working_time = datetime.datetime.utcnow()
    intersection, reachable_vertices = execute_query(args)
    print('intersection statistic:')
    for label, matrix in intersection.label_matrices.items():
        print('label: ', label, ': ', matrix.nonzero().nvals, ' - vertices amount')
    start_printing_working_time = datetime.datetime.utcnow()
    print('query execution time: ', (start_printing_working_time - start_working_time).microseconds, ' millis')
    print('reachable vertices')
    for i, j, _ in zip(*reachable_vertices.nonzero().to_lists()):
        print(j, ' reachable from ', i)
    end_working_time = datetime.datetime.utcnow()
    print('printing pairs time: ', (end_working_time - start_printing_working_time).microseconds, ' millis')
