print("\tWelcome to the Fibonacci Calculator App")
n = int(input("How many digits of the Fibonacci Sequence would you like to compute: "))
print("\nThe first 15 numbers of the Fibonacci sequence are:")
lista = [1,1]
for i in range(1,n):
    x=lista[i]+lista[i-1]
    lista.append(x)
for i in range(0,n):
    print(lista[i])
print("\nThe corresponding Golden Ratio values are:")

lista2 = []
for i in range(1,n+1):
    y = lista[i]/lista[i-1]
    lista2.append(y)
for i in range(1,n):
    print(lista2[i-1])
print("\nThe ratio of consecutive Fibonacci terms approaches Phi;1.61803398874989...")
