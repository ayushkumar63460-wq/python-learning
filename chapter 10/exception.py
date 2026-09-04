# age = int(input("Enter age: "))
# print(age)

''' if entered other value instead of any number then it shows this,
ValueError: invalid literal for int() with base 10: 'abc'''

# try:
#     age = int(input("Enter age: "))
#     print(f"Age is: {age}")
# except ValueError:
#     print("Please enter a valid number: ")

# try:
#     number = int(input("Number: "))
#     result = 10 / number

# except ValueError:
#     print("Enter a number.")

# except ZeroDivisionError:
#     print("You cannot divide by zero.")


'''else: '''
# try:
#     age = int(input("Enter age: "))
  
# except ValueError:
#     print("Please enter a valid number: ")
# else:
#     print(f"You entered:", {age})



'''finally'''
# try:
#    with open("data.txt", "r") as file:
#     data = file.read()
# except FileNotFoundError:
#   print("File Not Found...")

# finally:
#   print("Finished")



'''raise'''
#Sometimes you want to create an exception yourself.
age = -5
if age < 0:
  raise ValueError("Age Cannot be Negative")
else:
  print("Age is Valid")


'''try:
    # risky code

except SomeError:
    # handle error

else:
    # runs if try succeeded

finally:
    # always runs
    
raise SomeError("message") '''


'''try      → try risky operation
except   → handle failure
else     → handle success
finally  → cleanup regardless of outcome
raise    → deliberately signal an error'''