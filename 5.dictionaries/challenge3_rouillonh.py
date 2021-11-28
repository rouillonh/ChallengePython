print("\tWelcome to the Yes or No Issue Polling App")
#Pedimos el tema de la votación, la cantidad de votantes y la contraseña del admin
vote = input("\nWhat is the yes or no issue you will be voting on today: ")
v = int(input("What is the number of voters you will allow on the issue: "))
passw = input("Enter a password for polling results:")
""""Creamos las variables donde se contabilizaran los votos 
y tambien creamos el diccionario donde se amacenaran los votantes con su voto"""
af = 0
ec = 0
dic = {}
#Creamos el bucle para realizar la votación
for i in range(v):
    name = input("\nEnter your full name: ").title()
    if name not in dic:     
        print("Here is our issue:",vote)
        c = input("What do you think...yes or no: ").lower()
        if c.startswith('y'):
           print("Thank you, ",name ,"! Your vote of yes has been recorded.")
           af += 1
           dic[name] = 'yes'
        elif c.startswith('n'):
           print("Thank you, ",name ,"! Your vote of no has been recorded.")
           ec += 1
           dic[name] = 'no'
        else:
           print("That is not a yes or no answer, but okay...")
           print("Thank you ",name,"! Your vote of ",c,". has been recorded.")
    elif name in dic:
        print("Sorry, it seems that someone with that name has already voted.")
print("\nThe following ",len(dic.keys())," people voted: ")
for i in dic.keys():
    print(i)
print("\nOn the following issue:",vote)
if af > ec:
    print("Yes wins! ",af," votes to ",ec,".")
elif af < ec:
    print("No wins! ",ec," votes to ",af,".")
elif af == ec:
    print("It was a tie! ",af," votes to ",ec,".")
#Pedimos la contraseña para visualizar los resultados
passw2 = input("\nTo see the voting results enter the admin password: ")
if passw2 == passw:
    for clave,valor in dic.items():
        print("Voter: ",clave,"\t\tVote: ",valor)
else:
    print("Sorry, that is not the correct password. Goodbye...")
print("\nThank you for using the Yes or No Issue Polling App.")
