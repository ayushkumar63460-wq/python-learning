def avg():
    n1 = int(input("Enter your number:"))      # FUNCTION DEFENATION
    n2 = int(input("Enter your number:"))
    n3 = int(input("Enter your number:"))
    average = (n1+n2+n3)/3
    print(average)

#avg()          # FUCNTION CALL       

'''When a program gets bigger in size and its complexity grows, it gets difficult for a program to keep track
on which piece of code is doing what!
A function can be reused by the programmer in a given program any number of times '''


# def welcome(name):
     #name---> [ parameter ]
#  welcome("Ayush")
    #"Ayush"---> [Argument]

def welcome(name):                               
    print("Welcome", name)

welcome("Ayush")
welcome("Rahul")
welcome("Harry")