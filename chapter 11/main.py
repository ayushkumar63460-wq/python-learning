from class_variable import student

s1 = student("Charlie Kirk", 17)
s2 = student("Alice", 20)

print(s1.name)             #print from instance variables.
print(s1.age)
print(s2.name)
print(s2.age)
print(student.num_students)

print(s1.school)         #print from the class variables.


