#multiple inheritance: can inherit from more than one parent class.

class prey:
    def flee(self):
        print("This animal is fleeing..")

class predator:
    def hunt(self):
        print("This animal is hunting..")




class Rabbit(prey):
    pass

class Hawk(predator):
    pass

class Fish(prey, predator):          #Multiple Inherticance...
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

fish.hunt()
fish.flee()

