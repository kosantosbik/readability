#!/usr/bin/env python3

from readability import Readablity
from textract import process


def read_file(filename):
    "Opens a file and reads its contents"

    return process(filename).decode('utf-8')
