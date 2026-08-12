make = ["Orange", "Apple", "Pineapple","Coconut"]
make.append("Kiwi")                                   #append adds only one item to the end.
print(make)

make.extend(["Guava", "grapes"])                      #extend adds mutiple items to the end.
print(make)

make.insert(0,"DeezNutz")                             #insert adds a new item at you wanted index and lines goes another shift to right.
print(make)

make.remove("DeezNutz")                               #remove bruh it removes an item.
print(make)

make.pop()                      #pop yk like pops the wanted item like the cops does to blacks , if not selecte the item index then last one pops 
print(make) 
make.pop(3)
print(make) 

#make.clear()                                         #clear yk clears the entire list too bad for kkc lamao.                                    
#print(make)

print(make.index("Apple"))                            #index tell you where your item is.

print(make.count("Apple"))                            #count uk counts the occourances of an item in the list

make.sort()                                           #sort sorts the entire list in order alpahabeticlly or.....
print(make) 
like = [1,4,8,67,69,43,6,72,90,2]                     #numericals also nigg
like.sort()
print(like)

like.reverse()                                        #reverse cmon...
print(like)

like2 = like.copy()
print(like2) 
like2.append("45")
print(like2)
print(like)







