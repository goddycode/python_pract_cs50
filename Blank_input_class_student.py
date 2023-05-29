#!/usr/bin/python3
""" Same program as student program, but with blank input checking"""

class Student:
    def __init__(self, name, village):

        """Checking for black input and wrong village input"""
        if not name:
            raise ValueError("Name is missing ")
        if village not in ["Kawa", "Kaguka", "Adingo", "Ngege"]:
            raise ValueError("Invalid village")

        self.name = name
        self.village =village

    def __str__(self):
        return f"{self.name} from {self.village}"

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name ")
    village = input("Village ")

    return Student(name, village)

if __name__ == "__main__":
    main()


