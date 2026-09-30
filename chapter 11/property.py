



class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

#getter methods
    @property
    def width(self):
        return f"{self._width:.1f}cm"  

    @property
    def height(self):
        return f"{self._height:.1f}cm"   

#setter methods
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self.width = new_width
        else:
            print("width cannot be less than 0..")

    
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self.height = new_height
        else:
             print("Height cannot be less than 0..")


#delete methods
    @width.deleter
    def width(self):
        del self.width
        print("width has been deleted")
        

     




rectangle = Rectangle(20, 30)

rectangle.width = 10
rectangle.height = 15


del rectangle.width
del rectangle.height


print(rectangle.width)
print(rectangle.height)


