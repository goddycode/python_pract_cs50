#!/usr/bin/python3
"""

"""
def main():
    student = get_student()
    print(f"{student['name']} from {student['village']}")

def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["village"] = input("Village: ")
    
    return student

if __name__ == "__main__":
    main()
