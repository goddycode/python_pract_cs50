#!/usr/bin/python3
"""

"""
def main():
    student = get_student()
    if student[0] == "Goddy":
        student[1] = "Kaguka"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name ")
    village = input("Village ")

    return (name, village)

if __name__ == "__main__":
    main()
