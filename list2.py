#!/usr/bin/python3

"""
list methods
"""

list1 = list(( 1, 2, 3, 4, 5))

list2 = ['banana', 'mango', 'apple', 'mango', 'oranges']

students = list(('john', 'peter', 'sharon', 'catherine', 'caroline'))

print(students)

"""index() will list index no. of a particular 
item in a list"""
print(students.index("peter"))

"""append() will apend an item to a list"""
list1.append(9)

"""insert() will insert at the  specified index"""
list1.insert(3, 'cherry')

"""remove() will remove an item specified on list by its index"""
list1.remove(2)

"""Count the occurrence of the specified item"""
print(list2.count('mango'))

"""copy() will content of list2 to list3"""
list3 = list2.copy()

"""pop() wil delete the last item on the list"""
print(list3.pop())

"""Delete element at index 1"""
print(list3.pop(1) # or print(del3[1]

print(list2.sort())

print(list2.reverse())

##students.clear()

list1.extend(list2)

"""printing students after clear()"""
print(students)

print(list1)

