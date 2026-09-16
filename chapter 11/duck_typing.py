#It is another way to achieve polymorphism besides inheritance.
#objects must have minimum necesasarry attributeds/methods.
#"If is walks like a duck and quack like a duck then it must be a duck."

class Dog:
    def speak(self):
        print("Woof!")


class Cat:
    def speak(self):
        print("Meow!")


class Human:
    def speak(self):
        print("Hello!")


def make_sound(animal):
    animal.speak()   # We only care that .speak() exists


make_sound(Dog())    # Dog object → Woof!
make_sound(Cat())    # Cat object → Meow!
make_sound(Human())  # Human object → Hello!

#There is no inheritance b/w them yet this still works, that is duck typing it only cars about the common thing the speak here for instance.

