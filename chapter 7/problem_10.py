'''Write a program to print multiplication table of n using for loops in reversed order.'''

# For normal order of tables is usually like this:

'''n =int(input("Enter n:"))             # --->  This is normal,1 2 3 4 5 6  7 8 9 10... but want in reverse order the tbale for this:
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")'''

'''Reverse Order:'''
n = int(input("Enter n:"))
for i in range(1, 11):
    print(f"{n} x {11 - i} = {n*11-i}")

