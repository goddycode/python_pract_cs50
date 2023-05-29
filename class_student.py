#!/usr/bin/python3
"""


"""
class Student:
    def __init__(self, name, village):
        self.name = name
        self.village =village



def main():
    student = get_student()
    print(f"{student.name} from {student.village}")


def get_student():
    name = input("Name: ")
    village = input("Village: ")
    student = Student(name, village)

    return Student(name, village)

if __name__ == "__main__":
    main()
