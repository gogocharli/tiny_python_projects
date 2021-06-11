#!/usr/bin/env python3
"""
Author : Charles Yahouedeou <thexrayone@icloud.com>
Date   : 2021-06-10
Purpose: Return the line matching a letter input
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Return the line matching a letter input",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "letter",
        metavar="letter(s)",
        nargs="+",
        help="Letters to look for",
    )

    parser.add_argument(
        "-f",
        "--file",
        help="A readable file",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default="./gashlycrumb.txt",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    print(args.letter, args.file.name)


# --------------------------------------------------
if __name__ == "__main__":
    main()
