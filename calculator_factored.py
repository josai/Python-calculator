def PrintWelcomMessage():
    print ("Welcome")


def PrintInstruction():
    print("1 = Addition")
    print("2 = Subtraction")
    print("3 = Multiplication")
    print("4 = Division")
    print("5 = Modulo")
    print("6 = Exit program")


def PrintGoodbyeMessage():
    print ("Goodbye")


def Add(operation, x, y):
    return (x + y)


def Subtract(operation, x, y):
    return (x - y)


def Multiply(operation, x, y):
    return (x * y)


def Division(operation, x, y):
    '''
    Check for division by zero, if not then operate.
    '''
    if y == 0:
        return("Cannot divide by Zero.")
    else:
        return (x / y)


def Modulo(operation, x, y):
    '''
    Check for modulo by zero, if not then operate.
    '''
    if y == 0:
        return("Cannot modulo by Zero.")
    else:
        return (x % y)


def GetInput():
    Operation = int(input("Enter Calculator Operation: "))
    Operand1 = int(input("Enter first number: "))
    Operand2 = int(input("Enter second number: "))
    return (Operation, Operand1, Operand2)


def Operate(operation, x, y):
    '''
    Finds the proper operator and returns the result of that operation.
    '''
    if operation == 1:  # Addition code
        return (Add(operation, x, y))
    if operation == 2:  # Subtraction code
        return (Subtract(operation, x, y))
    if operation == 3:  # Multiplication code
        return (Multiply(operation, x, y))
    if operation == 4:  # Division code
        return (Division(operation, x, y))
    if operation == 5:  # Modulo code
        return (Modulo(operation, x, y))


def ValidateInput(operation, x, y):
    if operation >= 1 and operation <= 5:
        return (True)
    else:
        return (False)


def Main():
    PrintWelcomMessage()
    PrintInstruction()
    operation, x, y = GetInput()

    if operation == 6:
        print("User exit")
    else:
        validation_result = ValidateInput(operation, x, y)
        if not validation_result:
            exception_message = "invalid input"
            print("Exception raised:", exception_message)
        else:
            calculation_result = Operate(operation, x, y)
            print("Result of calculation =", str(calculation_result))
            PrintGoodbyeMessage()

if __name__ == "__main__":  # This part of code will execute first
    Main()
