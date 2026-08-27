'''Write a program to read the text from a given file ‘poems.txt’ and find out whether it
contains any particluar word'''

file = open("poem.txt", "r")
text = file.read()
if "continent" in text:
    print("True words exists..")
else:
    print("Word not present!!")
file.close()
