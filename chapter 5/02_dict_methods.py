person = {                     
    "name": "Ayush",
    "age": 17,
    "sex": "Male"
}


print(person.keys())         #Keys gives you the info of the left coloumn which is keys.

print(person.values())       #Values gives you the info of the right coloumn which is values.

print(person.items())        #items give you both thing keys and values.

print(person.get("Salary", "Not found"))   #get gives you the info whether that thing is avaliable about the thing or not without giving error and giving proper "none".

person.update({"age": 17})   #now update Updates existing keys or adds new ones.
print(person)
person.update({"Nationality": "Indian",
               "Work": "Student" })
print(person)

person.pop("age")           #now pop removes an item you want.
print(person)

person.popitem()           #Removes the last inserted key-value pair.
print(person)

#person.clear()            #Deletes everything.
#print(person)

person2 = person.copy()   #Creates another dictionary.
print(person2)

person.setdefault("country", "India")  #If this key doesn't exist, create it with this value. If it already exists, do nothing.
print(person)

person["Salary"] = 100000
print(person)