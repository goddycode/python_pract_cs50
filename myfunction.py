#!/usr/bin/python3

"""
python function
"""

def greetings():
    """This is a python greetings function"""

    name = input("Please input your name: ")

    age = input("Enter you age: ")

    print("Welcome {}, you are {} years old".format(name.title(), age))

greetings()


