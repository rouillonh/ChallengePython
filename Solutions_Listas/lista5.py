print("\tWelcome to the Favorite Teachers Program")
#Creamos una lista en blanco y preguntamos por los profesores favoritos
teacher = []
t1 = input("\nWho is your first favorite teacher? ").capitalize()
t2 = input("Who is your second favorite teacher? ").capitalize()
t3 = input("Who is your third favorite teacher? ").capitalize()
t4 = input("Who is your fourth favorite teacher? ").capitalize()
#Agregamos a la lista en blanco los nombres
teacher.append(t1)
teacher.append(t2)
teacher.append(t3)
teacher.append(t4)
#Mostramos en pantalla lo que nos piden
print("\nYour favorite teachers ranked are: ",teacher)
print("Your favorite teachers alphabetically are: ",sorted(teacher))
print("Your favorite teachers in reverse alphabetical order are: ",sorted(teacher)[ : :-1])
print("\nYour top two teachers are: ",teacher[0:2])
print("Your next two favorite teachers are: ",teacher[2:4])
print("Your last favorite teacher is: ",teacher[3])
print("You have a total of ",len(teacher)," favorite teacher")
#Agregamos un nuevo profesor favorito y lo mostramos en pantalla
t5 = input("Oops "+teacher[0]+" is no longer your first favorite teacher. Who is your new FAVORITE teacher: ").capitalize()
teacher[0] = t5
teacher[1] = t1
teacher[2] = t2
teacher[3] = t3
teacher.append(t4)
print("\nYour favorite teachers ranked are: ",teacher)
print("Your favorite teachers alphabetically are: ",sorted(teacher))
print("Your favorite teachers in reverse alphabetical order are: ",sorted(teacher)[ : :-1])
print("\nYour top two teachers are: ",teacher[0:2]) 
print("Your next two favorite teachers are: ",teacher[2:4])
print("Your last favorite teacher is: ",teacher[4])
print("You have a total of ",len(teacher)," favorite teacher")