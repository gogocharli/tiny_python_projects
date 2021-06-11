#!/usr/bin/env python3
"""
Author : Charles Yahouedeou <thexrayone@icloud.com>
Date   : 2021-06-11
Purpose: Find and Replace vowels in text
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Find and Replace vowels in text",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("input", metavar="text", help="Input text or file")

    parser.add_argument(
        "-v",
        "--vowel",
        help="Vowel to substitute",
        metavar="vowel",
        type=str,
        default="a",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    print(args.input)


# --------------------------------------------------
if __name__ == "__main__":
    main()
