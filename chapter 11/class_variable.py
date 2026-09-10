# Class Variables = Shared among all instances of a class.
#                   Defined outside the constructor.
#                   Allows you to share data among all objects created from that class.

class student:
    school = "ABC School"    #class variable
    num_students = 0

    
    def __init__(self, name, age):    #instance variable
        self.name = name
        self.age = age
        student.num_students += 1
