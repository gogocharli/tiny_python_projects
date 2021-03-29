#!/usr/bin/env python3
"""
Author : Charles Yahouedeou <thexrayone@icloud.com>
Date   : 2021-03-27
Purpose: Create an howling letter
"""

import argparse
from os import path


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Create an howling letter",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("input", metavar="input", help="the input string or file")

    parser.add_argument(
        "-o",
        "--outfile",
        help="The name of the output file. Will print there instead of the standard output",
        metavar="filename",
        type=str,
        default=None,
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    input = args.input
    out_file = args.outfile

    # Check if the input is a file
    is_file = path.isfile(input)

    out_str = ""
    if path.isfile(input):
        in_fh = open(input)
        out_str = in_fh.read().rstrip().upper()
    else:
        out_str = input.upper()

    if out_file != None:
        out_fh = open(out_file, "wt")
        out_fh.write(out_str)
        out_fh.close()
    else:
        print(out_str)


# --------------------------------------------------
if __name__ == "__main__":
    main()
