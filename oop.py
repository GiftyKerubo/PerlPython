class Fruits:
    # constructor method - used to initialize the attributes
    def __init__(self,name,price,color):
        self.name = name
        self.price = price
        self.color = color

        # method
    def display(self):
        print(f"I love eating {self.name}, it cost {self.price} and it is {self.color} in color")

# instance
myobj=Fruits("Bananas", 20, "yellow")
myobj.display()
myobj2=Fruits("mangoes", 40, "green")
myobj2.display()