'''Repeat program 4 for a list of such words to be censored.'''

words = ["donkey", "the", "that", "a"]


with open("file.txt", "r") as file:
    content = file.read()
for word in words: 
    content_new = content.replace(word, "#####")  

with open("file.txt", "w") as file:
    file.write(content_new)