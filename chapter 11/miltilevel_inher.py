#multilevel inheritance: inherit  from a parent class whcich inherits from another parent.


class Animal:                                   #Grandparent class
    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is Sleeping")




class prey(Animal):                                     #parent class
    def flee(self):
        print("This animal is fleeing..") 

class predator(Animal):                                 #parent class
    def hunt(self):
        print("This animal is hunting..")




class Rabbit(prey):                              #c1 (c= children)
    pass

class Hawk(predator):                            #c2
    pass

class Fish(prey, predator):            #c3               #Multiple Inherticance...
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

fish.hunt()
fish.flee()
rabbit.flee()
hawk.hunt()

rabbit.eat()
hawk.sleep()
