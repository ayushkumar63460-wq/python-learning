name = input("Enter Your Name:")

maths = float(input("Maths Marks:"))
physics = float(input("Physics Marks:"))
chem = float(input("Chemistry Marks:"))

average = (maths + physics + chem) / 3

if average >= 40:
    result = "PASS"
else:
    result = "FAIL"

print("Student:" , name)
print("Avergae:", average)
print("Result:", result)


'''Now Break this thing into functions so that have their own clean functions to do...'''

#1)Get the Student info..

def get_marks():
    maths = float(input("Maths: "))
    physics = float(input("Physics: "))
    chemistry = float(input("Chemistry: "))

    return maths, physics, chemistry


#2)Calculate the average of the subjects

def calculate_average(maths, physics, chemistry):
    return (maths+physics+chemistry ) / 3


#3)Check if pass or fail

def check_result(average):
    if average >= 40:
        return "PASS"
    return"FAIL"


#4) Display the result

def display_result(name, average, result):
    print("\nStudent:", name)
    print("Average:", average)
    print("Result:", result)


    
name = input("Enter your name: ")

maths, physics, chemistry = get_marks()

average = calculate_average(maths, physics, chemistry)

result = check_result(average)

display_result(name, average, result)





'''WAF to print the length of a list'''


cities  = ["Hyderabad", "Mumbai", "Delhi", "Kolkata", "Lucknow"]

def print_len(cities):
    print(len(cities))
print_len(cities)


def print_lent(cities):
    for city in cities:
        print(city, end= " ")

print_lent(cities)



'''WAF to print factorial of n'''


def fact_find(n):
    fact = 1
    for i in range(1, n+1):
      fact *= i
    print(fact)
     

fact_find(6)



'''WAF to convert USD to INR'''


def curr_converter(usd_value):
    inr_value = usd_value * 95.69
    print(usd_value, "USD =", inr_value, "INR")

curr_converter(23)