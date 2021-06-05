#!/usr/bin/env python3
"""tests for howler.py"""

import os
import re
import random
import string
import shutil
from subprocess import getstatusoutput, getoutput

prg = "./howler.py"


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return "".join(random.choices(string.ascii_letters + string.digits, k=k))


# --------------------------------------------------
def force_rmdir(directory):
    try:
        shutil.rmtree(directory)
    except OSError as e:
        print(f"Error: {e.filename} – {e.strerror}")


# --------------------------------------------------
def out_flag():
    """Either -o or --outdir"""

    return "-o" if random.randint(0, 1) else "--outdir"


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ["-h", "--help"]:
        rv, out = getstatusoutput(f"{prg} {flag}")
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_text_stdout():
    """Test STDIN/STDOUT"""

    out = getoutput(f'{prg} "foo bar baz"')
    assert out.strip() == "FOO BAR BAZ"


# --------------------------------------------------
def test_text_outfile():
    """Test STDIN/outfile in outdir"""

    out_dirname = random_string()
    if os.path.isdir(out_dirname):
        force_rmdir(out_dirname)

    try:
        out = getoutput(f'{prg} {out_flag()} {out_dirname} "foo bar baz"')
        assert out.strip() == ""
        text = open(os.path.join(out_dirname, "foo.txt")).read().rstrip()
        assert text == "FOO BAR BAZ"
    finally:
        if os.path.isdir(out_dirname):
            force_rmdir(out_dirname)


# --------------------------------------------------
def test_file():
    """Test file in/out"""

    for expected_file in os.listdir("test-outs"):
        try:
            out_dirname = random_string()
            if os.path.isdir(out_dirname):
                force_rmdir(out_dirname)

            basename = os.path.basename(expected_file)
            in_file = os.path.join("../inputs", basename)
            out = getoutput(f"{prg} {out_flag()} {out_dirname} {in_file}")
            assert out.strip() == ""
            produced = open(os.path.join(out_dirname, expected_file)).read().rstrip()
            expected = open(os.path.join("test-outs", expected_file)).read().strip()
            assert expected == produced
        finally:
            if os.path.isdir(out_dirname):
                force_rmdir(out_dirname)


# --------------------------------------------------
def test_lowercase_input():
    """Test text to lowercase instead of default"""

    out = getoutput(f'{prg} --ee "Foo Bar Baz"')
    assert out.strip() == "foo bar baz"
