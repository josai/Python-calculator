def add(operand1, operand2):
   return operand1 + operand2

def subtract(operand1, operand2):
   return operand1 - operand2

def multiply(operand1, operand2):
   return operand1 * operand2

def divide(operand1, operand2):
   return operand1 / operand2
   
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exit")

choice = int(input("Enter choice(1, 2, 3, 4, 5):"))
if choice == 5:
  print("goodbye")
  exit()
elif choice >= 6:
  print("invalid number")
  exit()

operand1 = (input("Enter first number: "))
operand2 = (input("Enter Second number: "))

if type(input) == "str":
    print ("invalid input")
    eixt()
elif type(input) == "int" or type (input) =="float": 
    print ("valid")

if choice == 1:
   print(operand1,"+",operand2,"=", add(operand1,operand2))

elif choice == 2:
   print(operand1,"-",operand2,"=", subtract(operand1,operand2))

elif choice == 3:
   print(operand1,"*",operand2,"=", multiply(operand1,operand2))

elif choice == 4:
  if operand2 <1:
          print("Sorry!no value can be divided by zero ")
  elif operand2>1:
   print(operand1,"/",operand2,"=", divide(operand1,operand2))

elif choice == 5:
   print("Goodbye")

else:
  print("invalid input")
  exit()
   
