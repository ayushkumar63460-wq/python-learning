'''Write a program to find out the line number where python is present from ques 6'''


with open("log.txt", "r") as file:
    lineno = 1

    for line in file:
        if "python" in line:
            print(f"Yes, Python is present in line no: {lineno}")
            break
        lineno += 1
    else:
        print("Python is not present...")


   
