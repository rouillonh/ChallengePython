print("\tWelcome to the Database Admin Program")
#Creamos el diccionario con los usernames y sus respectivas contraseñas
users = {
    'admin00':'admin1234',
    'mooman':'alskes145',
    'nickyD':'worl1star',
    'george2':'booo3oha',
    'meramo1986':'kehns010101'
}
#Preguntamos el username y vemos si esta o no en el diccionario
user = input("\nEnter your username: ")
if user not in users:
    print("Username not in database, goodbye.")
#Si está continua el programa y si no termina el programa
elif user in users:
    passw = input("Enter your password: ")
    if passw not in users.values():
       print("Password incorrect!")
    elif user == 'admin00':
       print("\nHello ",user,"! You are logged in!")
       print("\nHere is the current user database:")
       for clave,valor in users.items():
           print("Username: ",clave,"\t\tPassword: ",valor)
    elif user in users and user != 'admin00':
        print("\nHello ",user,"! You are logged in!")
        c = input("Would you like to change your password: ") 
        if c == 'yes':
            passw2 = input("What would you like your new password to be: ")
            if len(passw2) >= 8:
               print("\n",user," your password is ",passw2)
            elif len(passw2) < 8:
               print(passw2," not the minimum eight characters.")
               print("\n",user," your password is ",passw)
        elif c == 'no':
            print("Goodbye!")
        else:
            print("Invalid value")




