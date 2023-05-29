#!/usr/bin/python3
"""
Demonstrating use of sys library, len and argv
"""
import sys

if len(sys.argv) <2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)
