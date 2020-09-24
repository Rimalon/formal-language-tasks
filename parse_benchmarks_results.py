import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', required=True,
                        type=str, help='path to dir with benchmarks results')
    args = parser.parse_args()
    output_file = open('C:\\Users\\rimalon\\Desktop' + os.sep + 'outputLUBM.csv', "x")
    output_file.write('regex,ve_amount,query_ex_time,printing_time\n')
    for subdir, dirs, files in os.walk(args.dir):
        for filename in files:
            input_file = open(subdir + os.sep + filename)
            output_file.write(filename + '\n')
            for line in input_file.readlines():
                if not (line[0] == '[' or line[len(line) - 2] == ':' or line[len(line) - 2] == ' '):
                    line_words = line.split(' ')
                    if (line_words[0] == 'query'):
                        output_file.write(',' + line_words[4])
                    elif (line_words[0] == 'printing'):
                        output_file.write(',' + line_words[4] + '\n')
                    elif len(line_words) == 1:
                        regex_dirs = line_words[0].split('/')
                        regex_name = regex_dirs[len(regex_dirs) - 1]
                        output_file.write(regex_name[:len(regex_name) - 1])
                    else:
                        output_line = line_words[len(line_words) - 1]
                        output_file.write(',' + output_line[:len(output_line) - 1])

            input_file.close()
    output_file.close()
