run = True
while run:
    print("Print the South Asian Countries:")
    print(" ")
    listAsia = ['Pakistan', 'India', 'Maldive', 'Nepal', 'Sri Lanka', 'Bangldesh', 'Bhutan']
    print("1 = List of South Asian Countries")
    print("2 = Enter your choice")
    print("3 = Exit program")
    print(" ")
    cal = int(input("Enter number : "))

    
    if cal == 1:
      print(" ")
      print(listAsia)
      print(" ")
    elif cal == 2:
      print(" ")
      
    
      S_Asia = input("Please enter the first letter of the country name: ")
      print(" ")
      if S_Asia == "p":
        print('Pakistan')
        print(" ")
      elif S_Asia == "i":
        print('India')
        print(" ")
      elif S_Asia == "m":
        print('Maldives')
        print(" ")
      elif S_Asia == "n":
        print('Nepal')
        print(" ")
      
      elif S_Asia == "s":
        print('Sri Lanka')
        print(" ")
      elif S_Asia == "b":
        print('Bangladesh or Bhutan')
        print(" ")
        check = input("Enter the second letter of the Country")
        if check == "a":
          print("Bangladesh")
          print(" ")
        elif check == "h":
          print("Bhutan")
          print(" ")
      else: 
        print("Country doesn't belong to South Asia")
    elif cal == 3:
      print("Exit")
      run = False
      



