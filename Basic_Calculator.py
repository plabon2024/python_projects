def addition():
    num1 =float(input("Enter 1st Number:"))
    num2 = float(input("Enter 2nd Number:"))
    print(f"{num1}+{num2}= {num1 + num2}")

def subtraction():
    num1 = float(input("Enter 1st Number:"))
    num2 = float(input("Enter 2nd Number:"))
    print(f"{num1}-{num2}={num1-num2}")


def multiplication():
    num1 = float(input("Enter 1st Number:"))
    num2 = float(input("Enter 2nd Number:"))
    print(f"{num1}\u00D7{num2}={num1*num2}")

def division():
    num1 = float(input("Enter 1st Number:"))
    num2 = float(input("Enter 2nd Number:"))
    if num2 == 0:
        print("You Cannot divide by zero ")
    else:
        print(f"{num1}\u00F7{num2}={num1/num2}")


while True:
    print("""\n ****Basic Calculator***
    1.Addition
    2.Subtraction
    3.Multiplication
    4.Division
    0.Exit 
    """)


    try:
        option=int(input("Enter Option:"))
        if option==1:
            addition()
        elif option==2:
            subtraction()
        elif option==3:
            multiplication()
        elif option==4:
            division()
        elif option==0:
            print("Bye !")
            break
        else:
            print("Try using given number!")
    except Exception as e:
        print("Try again !")
