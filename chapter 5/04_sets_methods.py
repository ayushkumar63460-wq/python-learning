A = {1,3,6,8,9}
B = {6,7,10,5,4}

A.add(10)         #Adds one element.
print(A)

A.update([98, 71, 21])    #Adds multiple elements.
print(A)

A.remove(3)         #Removes an element.
print(A)

#Can also use (discard) instead of remove to be safe.

A.pop()         #Removes a random element.
print(A)

#Clear deletes everything

C = B.copy()        #Creates another set.
print(C)

print(A.union(B))     #Combines two sets.   same same    print(A | B)

print(A.intersection(C))      #Keeps only common elements.  print(A & B)

print(A.difference(C))          #Elements in A but not in B.     print(A - B)

print(A.symmetric_difference(B))     #Elements that are not common.   print(A ^ B)

print(A.issubset(B))               #Checks if every element of one set exists in another.

print(A.issuperset(C))          #Checks if one set contains all elements of another.

print(A.isdisjoint(B))         #Checks whether two sets have no common elements.

len(C)

# THESE WERE THE TOP 14 METHODS OF SETS.
