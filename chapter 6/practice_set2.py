subject1 = int(input("Enter your marks in Physics:"))
subject2 = int(input("Enter your marks in Chemistry:"))
subject3 = int(input("Enter your marks in Maths:"))

total = subject1 + subject2 + subject3
percentage = total/300 * 100

print("Your percentage is:", percentage)

if(percentage >= 40 and subject1 >= 33 and subject2 >= 33 and subject3 >= 33 ):
    print("PASS")
else:
    print("FAIL")


