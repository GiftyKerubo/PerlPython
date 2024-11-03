def addtwonumber():
    num=int(input("Enter First number"))
    num2=int(input("Enter Second number"))
    print(f"The sum of {num} and {num2} is {num+num2}")

# addtwonumber()

def multiplytwonumber():
    num3=int(input("Enter First number"))
    num4=int(input("Enter Second number"))
    print(f"The product of {num3} and {num4} is {num3*num4}")

# multiplytwonumber()
# calling it in calc and in this one will cause a loop

def perl_class(name,age,gender):
    print(f"Student Name is {name}, Age is {age} and {gender}".format(name,age,gender))
