'''Write a python program to rename a file to “renamed_by_python.txt”'''

with open("renameit.txt", "r") as file:
    content = file.read()

with open("renamed_by_python.txt", "w") as f:
    f.write(content)