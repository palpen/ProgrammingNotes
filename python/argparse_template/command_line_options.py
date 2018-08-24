"""
In command line:

python command_line_options.py -h

python command_line_options.py --file_path '/path/to/my/file.ext'

python command_line_options.py --file_path '/path/to/my/file.ext' \
                          --optional_args '/optional/input.ext'

python command_line_options.py --file_path '/path/to/my/file.ext' \
                          --optional_args '/optional/input.ext' \
                          --optional_noargs
"""

import argparse


def parse_args():

    # description shows up when invoking help option, -h
    parser = argparse.ArgumentParser(description="Basic application of argsparse in command line")

    parser.add_argument('-f', '--file_path', required=True,
                        help='This is a required argument that requires an input')

    parser.add_argument('-oa', '--optional_args', nargs=1,
                    help='This is an optional argument that requires an input (e.g. file name)')

    parser.add_argument('-ona', '--optional_noargs', action='store_true',
                        help='This is an optional argument that doesn\'t require any argument and' \
                        ' evaluate to True if option is provided')

    return vars(parser.parse_args())


if __name__ == '__main__':
    args = parse_args()

    print("Required with argument:", args['file_path'],
          "\nOptional but requires with argument:", args['optional_args'],
          "\nOptional but no argument:", args['optional_noargs'])
