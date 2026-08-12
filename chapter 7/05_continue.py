for i in range(1, 11):      #Skipped 6 entirely and continues from 7.
    if i == 6:
        continue
    print(i)

'''for example if i want to remove all the negative numbers from the numbers present in the list i can use this '''

numbers = [100, 88, -9, 67, -11, 4, -71, -1]
for number in numbers:
    if number < 0:
        continue

    print(number)


   
