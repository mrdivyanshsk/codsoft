print("                     CALCULATOR")

print("Arithematic operations will be in this format : eg.a+b")

def getprompta(promt):
    while True:
      try:
        value=float(input(promt))
        return value
      except:
        print("Invalid input... please enter a number")
 
a=getprompta("Enter the value of oprand a : ")

def getpromptb(promt):
    while True:
      try:
        value=float(input(promt))
        return value
      except:
        print("Invalid input... please enter a number")

b=getpromptb("Enter the value of oprand b : ")


x=float(input("Choose among four arithmetic operations\n1). Addition (+)\n2). Subtraction(-)\n3). Multiplication (*)\n4). Division (/)\n5). Exponential\nchoose your option : "))

match x :
  case 1 :
    try:
     print(f"{a} + {b} = {a+b}")
    except :
      print("error : you may have entered wrong thing in prompt")
  case 2 :
    try:
     print(f"{a} - {b} = {a-b}")
    except :
      print("error : you may have entered wrong thing in prompt")
  case 3 :
    try :
      print(f"{a} * {b} = {a*b}")
    except :
      print("error : you may have entered wrong thing in prompt")
  case 4 :
    try:
      print(f"{a} / {b} = {a/b}")
    except :
      print("error : division by zero is not allowed")
  case 5 :
    try:
      print(f"{a} ** {b} = {a**b}")
    except :
      print("error : you may have entered wrong thing in prompt")