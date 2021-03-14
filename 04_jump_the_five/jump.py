#!/usr/bin/env python3
"""
Author : Charles Yahouedeou <thexrayone@icloud.com>
Date   : 2021-01-24
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Encrypts numbers in a text by jumping the five",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "plaintext",
        metavar="plaintext",
        help="A string containing at least one integer",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Print string with jumped numbers"""

    args = get_args()
    input_str = args.plaintext

    jumper = {
        "0": "5",
        "1": "9",
        "2": "8",
        "3": "7",
        "4": "6",
        "5": "0",
        "6": "4",
        "7": "3",
        "8": "2",
        "9": "1",
    }

    encoded_text = input_str.translate(str.maketrans(jumper))

    print(encoded_text)


# --------------------------------------------------
if __name__ == "__main__":
    main()
