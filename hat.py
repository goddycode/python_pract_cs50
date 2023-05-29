#!/usr/bin/python3
"""
"""
class Hat:
    
    def __init__(self):
        self.houses = ["Adingo", "Kawa", "Kaguka", "Ngege"]
    def sort(self, name):
        print(name, "is in", random.choice(self.houses))

    hat = Hat()
    
    hat.sort("Harry")
