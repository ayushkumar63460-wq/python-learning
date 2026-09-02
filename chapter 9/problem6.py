'''Write a program to mine a log file and find out whether it contains ‘python’.'''

with open ("log.txt", "r") as file:
    content = file.read()

if ("Python" in content):
    print("Yes Python is there!")
else:
    print("Python Not present...")
    