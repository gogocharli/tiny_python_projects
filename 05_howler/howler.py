#!/usr/bin/env python3
"""
Author : Charles Yahouedeou <thexrayone@icloud.com>
Date   : 2021-03-27
Purpose: Create an howling letter
"""

import argparse
import sys
from os import path
import io


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

    args = parser.parse_args()
    if path.isfile(args.input):
        args.input = open(args.input)
    else:
        # Also treat a string as a stream,
        # the newline emulates a file's ending
        args.input = io.StringIO(args.input + "\n")

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    input = args.input
    out_file = open(args.outfile, "wt") if args.outfile else sys.stdout

    for line in input:
        out_file.write(line.upper())
    out_file.close()


# --------------------------------------------------
if __name__ == "__main__":
    main()
