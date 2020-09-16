import argparse
from src.main.paths_query_executor import execute_query

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--graph', required=True,
                        type=str, help='path to file with graph\nfile format:\n0 a 1\n0 b 2\n1 c 2')
    parser.add_argument('--query', required=True,
                        type=str, help='path to file with query\nfile format: regex in first line')
    parser.add_argument('--fr', required=False,
                        type=str, help='path to file with start vertices\nfile format:\n0 1 2')
    parser.add_argument('--to', required=False,
                        type=str, help='path to file with end vertices\nfile format:\n0 1 2')

    print(parser.usage)
    args = parser.parse_args()
    print(execute_query(args))