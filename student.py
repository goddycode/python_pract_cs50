#!/usr/bin/python3
"""
Demonstrating how to read values from csv file
"""
with open("student.csv") as file:
    for line in file:
        row=line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
