def check_number(n):
    if n > 0:
        return "Positive"
    else:
        return "Negative"
n = int(input("Enter n:" ))
result = check_number(n)
print(result)



def is_even(number):
    if number %2 == 0:
        return "Even"
    else:
        return "Odd"
number = int(input("Enter your number:"))
result = is_even(number)
print(result)



def check_age(age):
    if age >= 18:
        return "Adult"

    return "Minor"
age = int(input("Enter your age:"))
result = check_age(age)
print(result)



def check_temperature(t):
    if t >= 30:
        return "Hot"

    return "Normal"
t= float(input("Enter the temperature:"))
result = check_temperature(t)
print(result)



'''early return thing..'''
def check_password(password):
    if len(password) < 8:
        return "too short like your ....."
    
    return "Valid" 
password = (input("Enter your password:"))
result = check_password(password)
print(result)



def is_adult(age):
    return age >= 18

age = int(input("Enter your age: "))
result = is_adult(age)
print(result)
'''no need for this shit here age >= 18 already produces a boolean..
if age >= 18:
    return True
else:
    return False'''





def is_positive(number):
    return number > 0

def check_number(number):
    if is_positive(number):
        return "Postive number"

    return "Not Postive"
number = int(input("Enter your number:"))
result = check_number(number)
print(result)
