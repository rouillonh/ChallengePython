#Primero importamos la funcion factorial de la libreria math, luego la utilizaremos
from math import factorial
print("\tWelcome to the Factorial Calculator App")
#Pedimos un numero, para calcular su factorial
num = int(input("\nWhat number would you like to compute the factorial of? "))
fact = 1
#Creamos un bucle for para calcular el factorial con nuestro algoritmo
for i in range(1,num+1):
    fact *= i
#Imprimimos como es que se desarrollan las multiplicaciones
print(str(num)+"!=",end="")
for i in range(1,num):
    print(i,end="*")
print(str(num))
#Mostramos los resultados que nos lanzan nuestro algoritmo y la funcion factorial
print("\nHere is the result from the math library:")
print("The factorial of ",num," is ", factorial(num))
print("\nHere is the result from my own algorithm:")
print("The factorial of ",num," is ", fact)
print("\nIt is shown twice that ",num,"! = ",fact,"(with excitement)")
