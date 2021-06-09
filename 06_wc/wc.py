#!/usr/bin/env python3
"""
Author : Charles Yahouedeou <thexrayone@icloud.com>
Date   : 2021-06-04
Purpose: Count line, word, and bytes
"""

import argparse
import sys

DEFAULT_ARGUMENTS = ["lines", "words", "chars"]

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Count number of lines, words, and characters",
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

    parser.add_argument(
        "-l",
        help="Writes the number of lines to stdout",
        const="lines",
        dest="count_output",
        action="append_const",
    )

    parser.add_argument(
        "-w",
        help="Writes the number of words to stdout",
        const="words",
        dest="count_output",
        action="append_const",
    )

    parser.add_argument(
        "-c",
        help="Writes the number of characters to stdout",
        const="chars",
        dest="count_output",
        action="append_const",
    )

    args = parser.parse_args()

    return args


# --------------------------------------------------
def printResults(
    lines: str,
    words: str,
    chars: str,
    filename: str,
    output=None,
):
    if output is None:
        output = DEFAULT_ARGUMENTS

    lines_result = f"{lines:8}" if "lines" in output else ""
    words_result = f"{words:8}" if "words" in output else ""
    chars_result = f"{chars:8}" if "chars" in output else ""

    sys.stdout.write(
        "{}{}{} {}\n".format(lines_result, words_result, chars_result, filename)
    )


# --------------------------------------------------
def printTotal(total, output=None):
    if output is None:
        output = DEFAULT_ARGUMENTS

    lines_total = f"{total['lines']:8}" if "lines" in output else ""
    words_total = f"{total['words']:8}" if "words" in output else ""
    chars_total = f"{total['chars']:8}" if "chars" in output else ""

    sys.stdout.write(
        "{}{}{} {}\n".format(lines_total, words_total, chars_total, "total")
    )


# --------------------------------------------------
def main():
    """Word counter"""

    args = get_args()

    total = {"lines": 0, "words": 0, "chars": 0}

    for file in args.files:
        num_lines, num_words, num_chars = 0, 0, 0

        for line in file:
            num_words += len(line.split())
            num_chars += len(line)
            num_lines += 1

        total["lines"] += num_lines
        total["words"] += num_words
        total["chars"] += num_chars

        printResults(
            num_lines, num_words, num_chars, file.name, output=args.count_output
        )
        file.close()

    if len(args.files) > 1:
        printTotal(total, output=args.count_output)


# --------------------------------------------------
if __name__ == "__main__":
    main()
