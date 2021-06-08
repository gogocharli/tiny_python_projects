#!/usr/bin/env python3
"""
Author : Charles Yahouedeou <thexrayone@icloud.com>
Date   : 2021-06-04
Purpose: Count line, word, and bytes
"""

import argparse
import io
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
        type=argparse.FileType("rt"),
        nargs="*",
        default=[sys.stdin],
    )

    args = parser.parse_args()

    return args


# --------------------------------------------------
def count_words(string):
    """Return the word count of a string"""
    return len(string.split())


# --------------------------------------------------
def main():
    """Word counter"""

    args = get_args()

    total = {"num_lines": 0, "num_words": 0, "num_bytes": 0}

    for file in args.files:
        num_lines = 0
        num_words = 0
        num_bytes = 0

        for line in file:
            num_words += count_words(line)
            num_bytes += len(line)
            num_lines += 1

        total["num_lines"] += num_lines
        total["num_words"] += num_words
        total["num_bytes"] += num_bytes

        sys.stdout.write(
            "{:8}{:8}{:8} {}\n".format(num_lines, num_words, num_bytes, file.name)
        )
        file.close()
    if len(args.files) >= 2:
        sys.stdout.write(
            "{:8}{:8}{:8} {}\n".format(
                total["num_lines"], total["num_words"], total["num_bytes"], "total"
            )
        )


# --------------------------------------------------
if __name__ == "__main__":
    main()
