#Class is a protype or blueprint

class Calculator:
   num = 66

   def getData(self):
       print("Automation testing for data entry")

#come out of the class to call the funcn

#synthax to create objs
print(Calculator.num)
obj = Calculator()
obj.getData()
print(obj.num)