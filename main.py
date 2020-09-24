import argparse
import os
import time

from src.classes import Graph
from src.main.paths_query_executor import execute_query

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--graph', required=True,
                        type=str, help='path to file with graph\nfile format:\n0 a 1\n0 b 2\n1 c 2')
    parser.add_argument('--queries', required=True,
                        type=str, help='path to file with query\nfile format: regex in first line')
    parser.add_argument('--type', required=False,
                        type=str, help='sqr closure is default, set adj for adj closure')
    parser.add_argument('--fr', required=False, default=None,
                        type=str, help='path to file with start vertices\nfile format:\n0 1 2')
    parser.add_argument('--to', required=False, default=None,
                        type=str, help='path to file with end vertices\nfile format:\n0 1 2')
    args = parser.parse_args()
    graph = Graph.from_file(args.graph)
    for subdir, dirs, files in os.walk(args.queries):
        for filename in files:
            filepath = subdir + os.sep + filename
            print(filepath)
            queryGraph = Graph.from_regex_file(filepath)
            start_working_time = time.time()
            intersection, reachable_vertices = execute_query(args, graph, queryGraph)
            print('intersection statistic:')
            counter = 0
            for label, matrix in intersection.label_matrices.items():
                counter += matrix.nonzero().nvals
                # print('label: ', label, ': ', matrix.nonzero().nvals, ' - vertices amount')
            print(args.graph, ': vertices amount: ', counter)
            start_printing_working_time = time.time()
            print('query execution time: ', (start_printing_working_time - start_working_time), ' seconds')
            print('reachable vertices: ')
            print(list(map(lambda x: (x[1],x[0]), zip(*reachable_vertices.nonzero().to_lists()))))
            end_working_time = time.time()
            print('printing pairs time: ', (end_working_time - start_printing_working_time), ' seconds')
