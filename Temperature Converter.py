def cels_to_Fahr(c):
    f=c*(9/5)+32
    return f

def cel_to_kel(c):
    k=c+273.15
    return k

def kel_to_cel(k):
    c=k-273.15
    return c

def Kel_to_fahr(k):
    f=(k-273.15)*(9/5)+32
    return f

def fahr_to_kel(f):
    k=(f-32)*(5/9)+273.15
    return k

def fahr_to_cel(f):
    c=(f-32)*(5/9)
    return c

while True:
    try:
        print("""\n**** Temperature Converter *****
1.Enter the temperature value in Celsius
2.Enter the temperature value in Fahrenheit
3.Enter the temperature value in Kelvin""")
        option=int(input("Enter your choice (1/2/3):"))
        if option==1:
            c=int(input("Enter the temperature value in Celsius:"))
            print("""\n Choose the conversion
1. Celsius to Fahrenheit
2. Celsius to Kelvin
3. Both""")
            choice = int(input("Enter your choice (1/2/3): "))
            if choice == 1:
                print(f"{c}°C in Fahrenheit: {cels_to_Fahr(c)}°F")
            elif choice == 2:
                print(f"{c}°C in Kelvin: {cel_to_kel(c)}°F")
            elif choice == 3:
                print(f"{c}°C in Fahrenheit: {cels_to_Fahr(c)}°F")
                print(f"{c}°C in Kelvin: {cel_to_kel(c)}°F")

        elif option==2:
            f=int(input("Enter the temperature value in Fahrenheit:"))
            print("""\nChoose the conversion:
1. Fahrenheit to Celsius 
2. Fahrenheit to Kelvin
3. Both""")
            choice = int(input("Enter your choice (1/2/3): "))
            if choice==1:
                print(f"{f}°F in Celsius: {fahr_to_cel(f)}°F")
            elif choice==2:
                print(f"{f}°F in Kelvin: {fahr_to_kel(f)}°F")
            elif choice==3:
                print(f"{f}°F in Celsius: {fahr_to_cel(f)}°F")
                print(f"{f}°F in Kelvin: {fahr_to_kel(f)}°F")


        elif option==3:
            k=int(input("Enter the temperature value in Kelvin:"))
            print("""\n Choose the conversion:
1. Kelvin to Fahrenheit
2. Kelvin to Celsius
3. Both""")
            choice = int(input("Enter your choice (1/2/3): "))
            if choice==1:
                print(f"{k}°K in Fahrenheit: {Kel_to_fahr(k)}°F")
            elif choice==2:
                print(f"{k}°K in Celsius: {kel_to_cel(k)}°F")
            elif choice==3:
                print(f"{k}°K in Fahrenheit: {Kel_to_fahr(k)}°F")
                print(f"{k}°K in Celsius: {kel_to_cel(k)}°F")
        elif option==0:
            print("**** Bye ****")
            break


    except:
        print("Try again !")
