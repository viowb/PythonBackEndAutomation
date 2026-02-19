#Class variable,Instance variables, Methods, Constructor, Object usage
# Calculator class: blueprint for objects
class Calculator:
    num = 66  # class variable (shared by all objects)

    # Constructor (runs automatically when object is created)
    def __init__(self, a, b):
        self.firstNumber = a    # instance variable (unique to each object)
        self.secondNumber = b
        print("Constructor called: object created with values", a, "and", b)

    # Method to display a message
    def getData(self):
        print("I am executing a method in this class")

    # Method to calculate sum of instance variables + class variable
    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num




# -----------------------------
# Using the class

# Access class variable without creating an object
print("Class variable num:", Calculator.num)

# Create objects with different values
obj1 = Calculator(10, 20)
obj2 = Calculator(5, 15)

# Call methods
obj1.getData()
print("obj1 Summation:", obj1.Summation())

obj2.getData()
print("obj2 Summation:", obj2.Summation())

# Access class variable via objects
print("obj1.num:", obj1.num)
print("obj2.num:", obj2.num)
