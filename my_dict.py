#!/usr/bin/python3
"""
Dictionary is another data type just like list, str and tupple, but dict 
not accept duplicate of keys
"""
students = {"John": "Nairobi", 
        "Tom": "Migori", 
        "Otis": "Mombasa",
        }

print(students)

print(len(students))

print(type(students))

for student in students:
    print(student, students[student])
