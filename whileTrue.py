#!/usr/bin/python3
"""

"""
def main():
    number = get_number()
    meow(number)

main()

    def get_number():
        while True:
            n = int(input("What's a number? "))
            
            if n > 0:
                return n


    def meow(n):
        for _ in range(n):
