number = int(input("Enter your number:"))
if number > 1:
    for i in range(2, number):
        if number %i == 0:
            break
            print("Not a prime number....")
                
    else:
        print("Its a Prime number!!")
