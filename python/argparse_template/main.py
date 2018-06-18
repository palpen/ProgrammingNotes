# see https://gitlab.decisionsciences.bns/mosaic/label-generation
# how to use argparse with a json type configuration file
# usage: `python main.py config.json`

import argparse
import sys
import json


try:
    # Python 3.
    from json import JSONDecodeError
except ImportError:
    # Python 2 (ValueError is raised for JSON decoding problems).
    JSONDecodeError = ValueError

_PROGRAM_DESCRIPTION = \
    """How to use argparse
    """


def parse_args():
    """Parse and return the command-line arguments for the program.

    Returns
    -----------
    dict
        Arguments parsed from the command line.

    """
    parser = argparse.ArgumentParser(
        description=_PROGRAM_DESCRIPTION,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("config_file", help="path to the configuration file")
    return vars(parser.parse_args())


def main(configuration):

    print(configuration)

    #############################################################
    # Code that uses arguements stored in config.json goes here #
    #############################################################


if __name__ == '__main__':
    args = parse_args()
    try:
        with open(args['config_file']) as f:
            config = json.load(f)
    except IOError:
        sys.exit(1)
    except JSONDecodeError:
        sys.exit(1)

    main(config)
