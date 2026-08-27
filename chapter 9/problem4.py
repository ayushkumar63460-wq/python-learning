'''A file contains a word “Donkey” multiple times. You need to write a program which
replaces this word with ##### by updating the same file.'''


word = "donkey"

with open("file.txt", "r") as file:
    content = file.read()

content_new = content.replace("donkey", "#####")

with open("file.txt", "w") as file:
    file.write(content_new)