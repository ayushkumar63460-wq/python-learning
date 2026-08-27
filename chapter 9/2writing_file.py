'''Now writing a file in python only is good for writing in a empty file rather in writing in a Packed file 
cause it rewrites whatever was there in the file before writing again in python.'''

file = open(r"D:\coding_WD\PYTHON\text.txt.txt", "w")
text = file.write("python is actually fun...")
file.close()

#or
'''The best way to open and close the file automatically is the with statement.'''

with open(r"D:\coding_WD\PYTHON\text.txt.txt", "w") as file:
    text = file.write("Testing this out now...")
print(text)


'''Now there are different modes of opening a file:
 r - open for reading
w - open for writing
a - open for appending
+ - open for updating.
"rb" will open for read in binary mode.
"rt" will open for read in text mode.'''     

