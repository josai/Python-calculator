def PrintWelcomMessage():
    print ("Welcome")
    
def PrintInstruction():
    print("1 = Addition")
    print("2 = Subtraction")
    print("3 = Multiplication")
    print("4 = Division")
    print("5 = Exit program")


def PrintGoodbyeMessage():
    print ("Goodbye")
    
def Add(Operation, Operand1, Operand2):         #addition 
    return str(Operand1 + Operand2)

def Subtract(Operation, Operand1, Operand2):    #subtraction 
    return str(Operand1 - Operand2)

def Multiply(Operation, Operand1, Operand2):    #multipication
    return str(Operand1 * Operand2)

def Division(Operation, Operand1, Operand2):    #division, check for divide by zero 
    if Operand2==0:
        return "Cannot divide by Zero."
    else:
        return str(Operand1 / Operand2)    


def GetInput():
    Operation = int(input("Enter Calculator Operation: "))
    Operand1 = int(input("Enter first number: "))
    Operand2 = int(input("Enter second number: "))
    return Operation, Operand1, Operand2
    
def ValidateInput (Operation, Operand1, Operand2):
 
    if Operation >= 1 and Operation <= 5:
        ValidationResult = True
    else:
        ValidationResult=False

    return ValidationResult  #True or False

if __name__=="__main__":    #This part of code will execute first 
    PrintWelcomMessage()    #Print welcome message
    PrintInstruction()      #Print calculator instrucionts
          
    Operation, Operand1, Operand2 = GetInput()    #get input, operation, operand1 and 2
    
    ValidationResult = ValidateInput (Operation, Operand1, Operand2)    #validate input
    
    if ValidationResult:
        print("do normal things")

    else:
        if     Operation == 5:
            PrintGoodbyeMessage()
            #exit
        else:
            print("raise exception")
                
        