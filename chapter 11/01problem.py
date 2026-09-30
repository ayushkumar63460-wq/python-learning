#Write a class “Calculator” capable of finding square, cube and square root of a number.

import math

class Calculator:


    @staticmethod
    def greet(name):
        print(f"Hello, {name}!")

    def square(self, num):
        return num**2

    def cube(self, num):
        return num**3

    def sqrt(self, num):
        return math.sqrt(num)

c = Calculator()

c.greet("Max")
print(c.square(7))
print(c.cube(5))
print(c.sqrt(25))
    

