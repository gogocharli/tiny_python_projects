#!/usr/bin/env python3
"""
Author : Charles Yahouedeou <thexrayone@icloud.com>
Date   : 2021-01-15
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Stores and formats what you bring to a picnic",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "items", metavar="items", nargs="+", help="Item(s) to bring with you"
    )

    parser.add_argument(
        "-s", "--sorted", help="Sorts items by character", action="store_true"
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Prints the final list of items"""

    args = get_args()
    needs_sorting = args.sorted
    item_list = args.items

    if needs_sorting:
        item_list.sort()

    message = "You are bringing "

    if len(item_list) == 1:
        message += f"{item_list[0]}."
    elif len(item_list) == 2:
        message += f"{item_list[0]} and {item_list[1]}."
    else:
        message += f"{', '.join(item_list[0:-1])}, and {item_list[-1]}."
    print(message)


# --------------------------------------------------
if __name__ == "__main__":
    main()
