# Class is (blueprint) used to design the structure and layout of an object.
from car import Car

car1 = Car("Mustang", 2025, "Red", False)
car2 = Car("BMW", 2023, "Black", True)
car3 = Car("Honda", 2016, "Blue", False )

car1.drive()
car2.stop()

car1.describe()
car2.describe()
car3.describe()

