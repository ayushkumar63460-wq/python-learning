# open("filename", "mode")

file = open(r"C:\Users\acer\Documents\Anilist.txt", "r")
text = file.read()
print(text)
file.close()

'''HOW TO OPEN A FILE IN PYTHON
1) use the syntax to open the file it may be Realtive path or Absolute path.
2) now youve only opend a file not read it or printed it to display what is in it so 
   save it a text or any variable to use .read() to read it
3) now print the it using print(variable) 
4) now close the file after completing the work.'''


# Readline ( Read one line from the file.)
file = open(r"C:\Users\acer\Documents\Anilist.txt", "r")
line = file.readline()
print(line)


