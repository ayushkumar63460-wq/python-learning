'''while gets REALLY useful when the condition isn't a number range, for example,'''

password = ""
while password != "password123":
    password = (input("Enter your password:"))

    if password != "password123":
        print("incorrect password...")
else:
    print("Access Granted!")
