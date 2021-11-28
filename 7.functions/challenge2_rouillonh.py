def add(a,b):
    suma = round(a+b,4)
    print("The sum of ",a," and ",b," is ",suma)
    x =str(a)+"+"+str(b)+"="+str(suma)
    return x
def subtract(a,b):
    resta = round(a-b,4)
    print("The difference of ",a," and ",b," is ",resta)
    x = str(a)+"-"+str(b)+"="+str(resta)
    return x
def multiply(a,b):
    mult = round(a*b,4)
    print("The product of ",a," and ",b," is ",mult)
    x = str(a)+"*"+str(b)+"="+str(mult)
    return x
def divide(a,b):
    if b != 0:
        div = round(a/b,4)
        print("The quotient of ",a," and ",b," is ",div)
        x = str(a)+"/"+str(b)+"="+str(div)
        return x
    elif b == 0:
        print("You cannot divide by zero.")
        x = "DIV ERROR"
        return x
def exponent(a,b):
    exp = round(a**b,4)
    print("The result of ",a," raised to the ",b," power is", exp)
    x = str(a)+"**"+str(b)+"="+str(exp)
    return x
print("\tWelcome to The Python Calculator App")
print("Enter two numbers and an operation and the desired operation will be performed.")
historial = []
flag = True
while flag:
    a = int(input("\nEnter a number: "))
    b = int(input("Enter a number: "))
    op = input("Enter an operation (addition, subtraction, multiplication, division, or exponentiation): ").lower()
    if op.startswith("a") or op == "addition":
        c = add(a,b)
        historial.append(c)
    elif op.startswith("s") or op == "subtraction":      
        c=subtract(a,b)
        historial.append(c)
    elif op.startswith("m") or op == "multiplication":
        c=multiply(a,b)
        historial.append(c)
    elif op.startswith("d") or op == "division":
        c = divide(a,b)
        historial.append(c)
    elif op.startswith("e") or op == "exponent":
        c = exponent(a,b)
        historial.append(c)
    else:
        print("That is not a valid operation. Try again.")
        historial.append("OPP ERROR")
    c = input("Would you like to run the program again (y/n): ")
    if c == "y":
        flag = True
    elif c == "n":
        print("\nCalculation Summary:")
        for i in historial:
            print(i)
        print("Thank you for using The Python Calculator App. Goodbye.")
        flag = False
    
