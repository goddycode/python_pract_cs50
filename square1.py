#!/usr/bin/python3
"""Square class"""

class Square:
    def __init__(self, side):
        self.side = side

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        if value.isdigit():
            self.__side = value
        else:
    
def main():

        side = int(input("Please input the side: "))
        squ = Square()
        squ.side = side

        print("side :", squ.side)

        print("The Area of square :", squ.getArea())

main()

