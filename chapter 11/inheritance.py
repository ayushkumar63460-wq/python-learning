# Inheritance: Allows a class to inherit attributes and methods form another class.
               #Helps with code resuability and extensibility.
               
class Animals:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def walk(self):
        print(f"{self.name} is walking")




class dog(Animals):
    pass

class cat(Animals):
    pass

class mouse(Animals):
    pass


dog = dog("Scooby")
cat= cat("Garfield")
mouse = mouse("Mickey")



print(dog.name)                    # inheriting the attributes and the functions form the parent class
print(dog.is_alive)
cat.eat()
mouse.walk()
