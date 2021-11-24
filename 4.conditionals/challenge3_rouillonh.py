print("\tWelcome to the Voter Registration App")
#Pedimos nombre y edad para asi registrar su voto
name = input("\nPlease enter your name: ").title()
age = int(input("Please enter your age: "))
partidos = ['Republican','Democratic','Independent','Libertarian','Green']
#Si es mayor de edad, podrá votar
if age >= 18:
    #Dependiendo del partido que escoja, se imprimirá un mensaje
    print("\nCongratulations ",name,"! You are old enough to register to vote.")
    print("\nHere is a list of political parties to join.")
    for i in partidos:
        print("-",i)
    p = input("\nWhat party would you like to join: ").capitalize()
    if p in 'Republican,Democratic':
        print("Congratulations ",name,"! You have joined the ",p," party!")
        print("That is a major party!")
    elif p == 'Independent':
        print("Congratulations ",name,"! You have joined the ",p," party!")
        print("You are an independent person!")
    else:
        print("That is not a major party")
#Si no lo es, no podrá hacerlo
elif age < 18:
    print("You are not old enough to register to vote.")
