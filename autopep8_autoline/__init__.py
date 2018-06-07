#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Top-level package for autopep8-autoline."""

__author__ = """Adam Hitchcock"""
__email__ = 'adam@northisup.com'
__version__ = '0.1.0'


import re
import subprocess
import argparse
import autopep8
import sys
from functools import partial
from os import path


def run(cmd):
    # helper for subprocess.run
    return subprocess.run(cmd, shell=True, stdout=subprocess.PIPE).stdout.decode('utf8')


def all_changed(suffix='.py'):
    # get all changed files in the repo that end in .py
    yield from (
        f for f in run('git diff --name-only --relative HEAD').split('\n')
        if f.endswith(suffix)
    )


def get_files():
    # get all files with default argument of nothing being all files
    args = autopep8.create_parser().parse_args()
    if args.files:
        yield from args.files
    else:
        yield from all_changed()


def get_changed_lines(f, reverse=True, as_type=str):
    # given a file return all changed lines
    lines = run('git diff -U0 HEAD -- "{}"'.format(f)).split('\n')
    r = re.compile(r'@@\s+-?\d+\s+\+?(\d+)(?:,(\d+))?')

    numbers = (
        r.match(line).groups()
        for line in lines
        if line.startswith('@@')
    )

    if reverse:
        numbers = reversed(list(numbers))

    for start, count in numbers:
        start, count = as_type(start), as_type(count or 0)
        yield start, start + count


def main():
    # wrap autopep8.main
    for f in get_files():
        for range in get_changed_lines(f):
            autopep8.main(sys.argv + ['--line-range', *range, f])


if __name__ == '__main__':
    main()