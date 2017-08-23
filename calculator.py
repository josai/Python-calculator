#This is a change on line 1 
run = True 

while run:
    print("1 = Addition")
    print("2 = Subtraction")
    print("3 = Multiplication")
    print("4 = Division")
    print("5 = Exit program")
    cal = int(input("Enter number : "))
    if cal == 1:
        print("Addition")
        first = int(input("Enter first number :"))
        secund = int(input("Enter secund number :"))
        result = first + secund
        print("result =" , result)
    elif cal == 2:
        print("Subtraction")
        first = int(input("Enter first number :"))
        secund = int(input("Enter secund number :"))
        result = first - secund
        print("result =" , result)
    elif cal == 3:
        print("Mmltiplication")
        first = int(input("Enter first number :"))
        secund = int(input("Enter secund number :"))
        result = first * secund
        print("result =" , result)
    elif cal == 4:
        print("Division")
        one = int(input("Enter first number :"))
        two = int(input("Enter secund number :"))
        if two <1:
          print("Sorry!no value can be divided by zero ")
        elif two>1:
          result = one / two
          print("result =" , result)
    elif cal == 5:
        print("Quit!")
        run = False


