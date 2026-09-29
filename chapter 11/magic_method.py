# Dunder methods __init__, __str__, __eq__...
#They are automatically called by many of python's builtin operations.
#They allow devs to define or customize the behaviour of objects.


class Student:

    def __init__(self, name):
        self.name = name
#So __init__ is about initial setup.

    def __str__(self):
        return f"Student: {self.name}"
#"When you need a human-readable string for this object, use this."

    def __len__(self):
        return len(self.name)
#"Tell Python what the size/length of my object means."   

s = Student("John")
print(s)
print(len(s))
    


# class Money:

#     def __init__(self, amount):
#         self.amount = amount

#     def __add__(self, other):
#         return Money(self.amount + other.amount)

# m1 = Money(int(input()))
# m2 = Money(int(input()))

# m3 = m1+m2
# print(m3.amount)
#"Define what + means when my object is involved."

'''same with all these
a - b    → __sub__
a * b    → __mul__
a / b    → __truediv__
a // b   → __floordiv__
a % b    → __mod__
a ** b   → __pow__'''



class Teachers:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name ==  other.name  

n1 = Teachers("Max")
n2 = Teachers("Max")

print(n1.__eq__(n2))
#"Define what equality means for my objects."


'''other equality methods:
a == b   → __eq__
a != b   → __ne__
a < b    → __lt__
a <= b   → __le__
a > b    → __gt__
a >= b   → __ge__'''

