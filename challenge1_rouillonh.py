#Damos la bienvenida y pedimos nombre al usuario
print("\tWelcome to the Letter Count App")
name = input("\nWhat is your name? ").title()
print("\nHello! ",name)
print("I will count the number of times that a specific letter occours in a message")
#Pedimos la frase y la letra a contar
mens = input("\nPlease enter a message: ")
letter = input("Which letter would you like to count the occurrences of: ")
#Mostramos lo que nos pide
print(name," your message has ",mens.count(letter)," ",letter,"'s in it")