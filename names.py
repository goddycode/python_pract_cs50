#!/usr/bin/python3
"""
"""

names = []
for _ in range(3):
    name = input("what's your name?")
    names.append(name)

for name in sorted(names):
    print(f"hello {name}")
