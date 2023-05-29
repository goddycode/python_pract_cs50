#!/usr/bin/python3
"""A simple program to print 'hello world'"""

name = input("Whats your name? ").strip().title()

#Split user's name int first name and last name
first, last = name.split(" ")

print(f"Hello, your full: {name}, first name : {first} and last name: {last}")
