#!/usr/bin/env python3
"""tests for picnic.py"""

import os
from subprocess import getoutput

prg = "./picnic.py"


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ["", "-h", "--help"]:
        out = getoutput(f"{prg} {flag}")
        assert out.lower().startswith("usage")


# --------------------------------------------------
def test_one():
    """one item"""

    out = getoutput(f"{prg} chips")
    assert out.strip() == "You are bringing chips."


# --------------------------------------------------
def test_two():
    """two items"""

    out = getoutput(f'{prg} soda "french fries"')
    assert out.strip() == "You are bringing soda and french fries."


# --------------------------------------------------
def test_more_than_two():
    """more than two items"""

    arg = '"potato chips" coleslaw cupcakes "French silk pie"'
    out = getoutput(f"{prg} {arg}")
    expected = (
        "You are bringing potato chips, coleslaw, " "cupcakes, and French silk pie."
    )
    assert out.strip() == expected


# --------------------------------------------------
def test_two_sorted():
    """two items sorted output"""

    out = getoutput(f"{prg} -s soda candy")
    assert out.strip() == "You are bringing candy and soda."


# --------------------------------------------------
def test_more_than_two_sorted():
    """more than two items sorted output"""

    arg = "bananas apples dates cherries"
    out = getoutput(f"{prg} {arg} --sorted")
    expected = "You are bringing apples, bananas, cherries, and dates."
    assert out.strip() == expected


# ---------------------------------------------------
def test_no_oxford_comma():
    """does not include the oxford comma when printed out"""

    arg = "juice marshmellows napkins"
    out = getoutput(f"{prg} {arg} --no-oxford")
    expected = "You are bringing juice, marshmellows and napkins."
    assert out.strip() == expected


# ---------------------------------------------------
def test_support_custom_seperator():
    """Allow the user to pass a seperator of their choosing"""

    arg = "crabs sushi shawarmas tacos"
    out = getoutput(f"{prg} {arg} -c ';'")
    expected = "You are bringing crabs; sushi; shawarmas; and tacos."
    assert out.strip() == expected