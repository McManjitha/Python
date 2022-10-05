def getInput(num):
    value = input("Enter "+num+" number: ")
    if value[len(value)-1] == '$':
        return '$'
    return value

    
def select_op(choice):
    if choice == '#':
        return -1
    else:
        try:
            a = getInput('first')
            if a == '$':
                return 0
            a = float(a)
            b = getInput('second')
            if b == '$':
                return 0
            b = float(b)
        except:
            return -1

        if choice == '+':
            print(f'{a} {choice} {b} = {a+b}')
        elif choice == '-':
            print(f'{a} {choice} {b} = {a-b}')
        elif choice == '*':
            print(f'{a} {choice} {b} = {a*b}')
        elif choice == '/':
            if b == 0:
                print("float division by zero")
                print(f'{a} {choice} {b} = None')
            else:
                print(f'{a} {choice} {b} = {a/b}')
        elif choice == '^':
            print(f'{a} {choice} {b} = {a**b}')
        elif choice == '%':
            print(f'{a} {choice} {b} = {a%b}')
        
        
    

while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()
  else:
      continue