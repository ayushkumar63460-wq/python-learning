#Decorator = A function that extends the behavior of another function
#w/o modifying the base function
#Pass the base function as an argument to the decorator


#this is a dectorator
def add_sprinkles(func):
    def wrapper():
        print("*you add sprinkles*")
        func()
    return wrapper

#my base function
@add_sprinkles
def get_ice_cream():
    print("Here is your ice cream")

get_ice_cream()

