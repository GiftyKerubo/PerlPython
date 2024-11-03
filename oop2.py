# create a class called person with name, age, and gender as
# the attribute, a constructor, a method and a object

class Person:
    def __init__(self, name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(f"My name is {self.name}, I am {self.age} years old, and my gender is {self.gender}")

myobj3=Person("Gift",23,"Female")
myobj3.display()
myobj4=Person("Frank",24,"Male")
myobj4.display()
myobj5=Person("Antony",24,"Male")
myobj5.display()
