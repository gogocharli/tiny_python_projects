#!/usr/bin/env python3
"""
Author : Charles Yahouedeou <thexrayone@icloud.com>
Date   : 2020-12-26
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_parser():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(description="Chooses the correct article")

    parser.add_argument(
        "word", metavar="word", help="must start with an alphabetical character"
    )
    parser.add_argument(
        "-s",
        "--side",
        metavar="side",
        default="larboard",
        help="which side of the boat",
    )

    return parser


# --------------------------------------------------
def main():
    """Prints the appropriate message"""
    vowels = ("a", "e", "i", "o", "u")

    parser = get_parser()
    args = parser.parse_args()
    word = args.word
    side = args.side

    if word[0].isalpha():
        article = "an" if word.lower().startswith(vowels) else "a"
        article = article.capitalize() if word.istitle() else article

        print(f"Ahoy, Captain, {article} {word} off the {side} bow!")
    else:
        parser.print_help()
        exit(1)


# --------------------------------------------------
if __name__ == "__main__":
    main()
