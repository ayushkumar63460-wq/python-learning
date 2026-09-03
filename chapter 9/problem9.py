'''Write a program to find out whether a file is identical and matches the content of anotherfile'''

with open("file1.txt") as file:
    content1 = file.read()

with open("file2.txt") as file:
    content2 = file.read()

if content1 == content2:
    print("identical Content found on both files!!")
else:
    print("No files are not identical...")

    