#!/usr/bin/env python3
"""
Author : Charles Yahouedeou <thexrayone@icloud.com>
Date   : 2021-06-04
Purpose: Count line, word, and bytes
"""

import argparse
import sys
from os import path


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Count line, word, and bytes",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "files",
        help="Input file(s)",
        metavar="FILE",
        nargs="*",
        default=sys.stdin,
    )

    args = parser.parse_args()
    args.files = [open_file(file) for file in args.files]

    return args


# -------------------------------------------------
def open_file(filename):
    """Opens a file if it exists"""
    if path.isfile(filename):
        return (filename, open(filename))
    else:
        sys.exit(f"No such file or directory: '{filename}'")


# --------------------------------------------------
def count_words(string):
    """Return the word count of a string"""
    return len(string.split())


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for (filename, file) in args.files:
        lines = 0
        words = 0

        for line in file:
            words += count_words(line)
            lines += 1
        sys.stdout.write(f"{words:>4} {lines:>4} {filename}\n")
    file.close()


# --------------------------------------------------
if __name__ == "__main__":
    main()
