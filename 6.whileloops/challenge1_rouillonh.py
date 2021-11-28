print("\tWelcome to the Factor Generator App")
#Creamos la variable c = True para utilizar en un bucle sin fin
c = True
#Creamos el bucle
while c :
    num = int(input("\nEnter a number to determine all factors of that number: "))
    fact = []
    #Añadimos los factores del número
    for i in range(1,num+1):
        if num%i == 0:
            fact.append(i)
    print("\nFactors of ",num ," are:")
    #Mostramos los factores y la multiplicacion
    for i in fact:
        print(i)
    print("\nIn summary:")
    for i in fact:
        for j in fact:
            if i*j==num and i<=j:
                print(i,"*",j," = ",num)
    s = input("Run again (y/n): ").lower()
    if s == 'yes':
        continue
    if s == 'no':
        print("\nThank you for using the program. Have a great day.")
        break
