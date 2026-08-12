number = int(input("Enter your number:"))
stop = int(input("Enter where to stop: "))
for i in range(1, stop+1):
    print(number * i)

'''THIS IS THE TABLE OF ANY NUMBER THE USER ENTERS USING FOR Loop.'''

# OR it can be also done like this:

n = int(input("Enter your number:"))
stop = int(input("Enter your number:"))
for i in range(1, stop+1):
    print(f"{n} x {i} = {n*i}") 