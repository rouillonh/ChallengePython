#Importamos la libreria time
from time import time
print("\tWelcome to the Prime Number App")
#Creamos esta variable para el bucle sin fin
band = True
while band:
    print("\nEnter 1 to determine if a specific number is prime.")
    print("Enter 2 to determine all prime numbers within a set range.")
    choice = input("Enter your choice 1 or 2: ")
    #Ponemos las condicionales entre las opciones
    if choice == "1":
        num = int(input("\nEnter a number to determine if it is prime or not: "))
        if num>=2:
            prime_status = True
            for i in range(2,num):
                if num%i==0 or num<2:
                   prime_status = False
            if prime_status == True:
                print(num," is prime")
            elif prime_status == False:
                print(num," is not prime")
        elif num<2 and num>=0:
            print(num," is not prime")
    if choice == "2":
        n1 = int(input("\nEnter the lower bound of your range: "))
        n2 = int(input("Enter the upper bound of your range: "))
        primos = []
        start_time = time()      
        for i in range(n1,n2):
            prime_status = True
            if n1>=1:
                for j in range(2,i):
                    
                    if i ==j:
                        break
                    elif i%j==0:
                        prime_status=False
                    else:
                        continue   

                if prime_status == True:
                    primos.append(i)
            if i == 1:
                primos.remove(i)
        end_time = time()
        delta_time = end_time - start_time
        print("\nCalculations took a total of ",round(delta_time,5) ," seconds.")
        print("The following numbers between ",n1," and ",n2 ," are prime:")
        for i in primos:
            print(i)
        print("Press enter to continue")
        input()
        

    elif choice != "1" and choice != "2":
        print("\nThat is not a valid option.")
    c = input("Would you like to run the program again (y/n): ").lower()
    #Preguntamos si quiere continuar con el programa
    if c == 'y':
        continue
    elif c == 'n':
        print("\nThank you for using the program. Have a nice day.")
        break

        

        
            
                

