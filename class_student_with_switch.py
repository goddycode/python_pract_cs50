#!/usr/bin/python3
""" Same as the student class, but this is using switch statement
"""
class Student:
    def __init__(self, name, village, patronus):
        if not name:
            raise ValueError("missing name")
        if village not in ["kawa", "adingo", "ngege", "kaguka"]:
            raise ValueError("Invalid Village")
        self.name = name
        self.village = village
        self.patronus = patronus
    
    def __str__(self):
        return f"{self.name} from {self.village}"

    def charm(self):
        match self.patronus:
            case "Hash":
                return "#"
            case "Each":
                return "@"
            case "Percentage":
                return "%"
            case "dollar":
                return "$"
            case _:
                return "*"

def get_student():
    name = input("Name")
    village = input("Village")
    patronus = input("Patronus")

    return Student(name, village, patronus)

def main():
    student = get_student()
    print("Computer symbols are as follows: ")
    print(f"{student.patronus}")

if __name__ == "__main__":
main()
