#!/usr/bin/env python3
"""
Author : Charles Yahouedeou <thexrayone@icloud.com>
Date   : 2021-03-27
Purpose: Create an howling letter
"""

import argparse
import sys
import os
import io


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Create one or more howling letters",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "input", nargs="+", metavar="input", help="file or string input(s)"
    )

    parser.add_argument(
        "-o",
        "--outdir",
        help="The name of the output directory",
        metavar="directory",
        type=str,
        default=None,
    )

    parser.add_argument(
        "-e",
        "--ee",
        help="Converts the text to lowercase instead of uppercase",
        action="store_true",
        dest="lower",
    )

    args = parser.parse_args()

    args.input = [input_to_stream(input) for input in args.input]
    return args


# --------------------------------------------------
def input_to_stream(input):
    if os.path.isfile(input):
        return (os.path.basename(input), open(input))
    else:
        return (f"{input[0: 3]}.txt", io.StringIO(input + "\n"))


# --------------------------------------------------
def change_case(text, lower=False):
    """Transform text to uppercase or lowercase"""
    return text.lower() if lower else text.upper()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    input = args.input
    outdir = args.outdir

    # Create the directory if it doesn't exist
    if outdir and not os.path.isdir(outdir):
        os.mkdir(outdir)

    # For each file in the input list write a new file
    for (filename, file) in input:
        out_file = open(os.path.join(outdir, filename), "wt") if outdir else sys.stdout

        for line in file:
            out_file.write(change_case(line, lower=args.lower))

        # Only close if there is an output file
        if outdir:
            out_file.close()


# --------------------------------------------------
if __name__ == "__main__":
    main()
