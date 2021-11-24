print("\nWelcome to the Average Calculator App")
name = input("What is your name? ").title()
n = int(input("How many grades would you like to enter: "))
lista = []
for i in range(n):
    a = int(input("Enter grade: "))
    lista.append(a)
print("\nGrades Highest to Lowest:")
for i in sorted(lista,reverse=True):
    print("\t",i)
suma = 0
for i in lista:
    suma+=i
print("\n",name,"'s Grade Summary:")
print("\tTotal Number of Grades: ",n)
print("\tHighest Grade: ",sorted(lista,reverse=True)[0])
print("\tLowest Grade: ",sorted(lista,reverse=True)[n-1])
print("\tAverage: ",suma/n)
d= int(input("\nWhat is your desired average: "))
print("\nGood luck Mike!")
print("You will need to get a ", 6*d-suma ," on your next assignment to earn a ", d," average.")
print("\nLets see what your average could have been if you did better/worse on an assignment.")
x = int(input("What grade would you like to change? "))
print("What grade would you like to change ",x," to: ",end="")
m = int(input())
lista2 = lista.copy()
lista2.remove(x)
lista2.append(m)
suma2 = 0
for i in sorted(lista2,reverse=True):
    print("\t",i)
for i in lista2:
    suma2+=i
print("\n",name,"'s New Grade Summary:")
print("\tTotal Number of Grades: ",n)
print("\tHighest Grade: ",sorted(lista,reverse=True)[0])
print("\tLowest Grade: ",sorted(lista,reverse=True)[n-1])
print("\tAverage: ",suma2/n)
print("\nYour new average would be a ",suma2/n," compared to your real average of ",suma/n,"!")
print("That is a change of ",round(suma2/n - suma/n,2), "points!")
print("\nToo bad your original grades are still the same!")
print(sorted(lista,reverse=True))
print("You should go ask for extra credit!")