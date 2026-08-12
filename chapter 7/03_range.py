for i in range(7):  #stops before 7 in 6.
    print(i)

for i in range(9, 17): #(start, stop) in the rage start at 9 and stop before 17.
    print(i)


'''range(start, stop, step)'''
#Now you can tell Python how much to jump each time.

for i in range(2, 21, 2):    #Table of 2. here step is 2 so numbers jumps 2 evrytime.
    print(i)

# Can also go backwards with this for example,

for i in range(10, 0, -1):  #10 to 1 backwards.
    print(i)


# Can also use else function with the for loop for example,

for i in range(2, 21, 2):
    print(i)
else:
    print("Done")
