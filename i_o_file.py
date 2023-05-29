#!/usr/bin/python3
"""

"""
name = input("what's your name?")

with open("name.txt", "a") as file:
    file.write(f"{name}\n")
