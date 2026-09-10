class Car:
    def __init__(self, model, year, color, for_sale):               #ATTRIBUTES(variables)
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale


    def drive(self):
        print(f"You are driving {self.model}")                    #METHODS(functions)

    def stop(self):
        print(f"you stopped the car {self.model}")

    def describe(self):
        print(f"You drive the car {self.model} in {self.color} made in {self.year} and is not for sale")


        