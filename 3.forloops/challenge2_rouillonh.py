#Importamos la libreria math, luego la utilizaremos en el cálculo
from math import sqrt 
print("\tWelcome to the Quadratic Equation Solver App.")
print("\nA quadratic equation is of the form ax^2 + bx + c = 0")
print("Your solutions can be real or complex numbers.")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and bj is the imaginary portion.")
#Pedimos cuantas ecuaciones se van a calcular
n = int(input("How many equations would you like to solve today: "))
x1 = 0
x2 = 0
#Creamos el bucle for para el calculo de las raices
for i in range(1,n+1):
    print("\nSolving equation #",i)
    print("----------------------------")
    a = float(input("Please enter your value of a (coefficient of x^2): "))
    b = float(input("Please enter your value of b (coefficient of x): "))
    c = float(input("Please enter your value of c (coefficient): "))
    discriminante = (b**2)-(4*a*c)
    print("\nThe solutions to ",a,"x^2 + ",b,"x + ",c,"= 0 are:")
    #Aqui se utiliza el condicional ya que la raiz puede ser compleja 
    if discriminante > 0:
        x1 = (-b+sqrt(discriminante))/(2*a)
        x2 = (-b-sqrt(discriminante))/(2*a)
        print("x1 = (",x1,"+0j)")
        print("x2 = (",x2,"+0j)")
    elif discriminante == 0:
        x1 = -b/(2*a)
        x2 = -b/(2*a)
        print("x1 = (",x1,"+0j)")
        print("x2 = (",x2,"+0j)")
    elif discriminante < 0:
        real = -b/(2*a)
        imag = (sqrt(discriminante*(-1)))/(2*a)
        print("x1 = (",real,"+",imag,"j)")
        print("x2 = (",real,"-",imag,"j)")
print("Thank you for using the Quadratic Equation Solver App. Goodbye.")
