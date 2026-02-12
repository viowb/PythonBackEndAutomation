#Class is a protype or blueprint

class Calculator:
   num = 66

   # default constructor
   def __init__(self, a, b):
       self.firstNumber = a
       self.secondNumber = b
       print("Constructor called when objects are created")

   def getData(self):
       print("I am executing a method in this class")

   def Summation(self):
       return self.firstNumber + self.secondNumber + Calculator.num

   def getData(self):
       print("Automation testing for data entry")

#<=come out of the class to call the funcn

# Access class variable without creating an object
print(Calculator.num)

#synthax to create objs

# Create an object and pass values for constructor
obj = Calculator(10, 20)
# Call object methods
obj.getData()
print(obj.num)           # class variable via object
print(obj.Summation())   # method that sums values



