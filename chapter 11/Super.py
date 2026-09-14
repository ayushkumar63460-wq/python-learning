# Super= Super() = Function used in child class to call methods from a parent class(Superclass).
#        Allows you to extend the functionality of the inherited methods.

class Shape:                                             #Parent class(Super class)
      def __init__(self,color, is_filled):
            self.color = color
            self.is_filled = is_filled


class Circle(Shape):
    def __init__(self, color, is_filled, radius):            #(sub-super class)
        super().__init__(color, is_filled)
        self.radius = radius

class Sqaure(Shape):
     def __init__(self, color, is_filled, width):
            super().__init__(color, is_filled)
            self.radius = width

class Triangle(Shape):
      def __init__(self, color, is_filled, width, height):
             super().__init__(color, is_filled)
             self.radius = width
             self.height = height



circle = Circle("Red", True, 30)
