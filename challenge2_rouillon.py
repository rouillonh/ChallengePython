#Damos la bienvenida al usuario
print("\tWelcome to the Miles Per Hour Conversion App")
#Pedimos el valor del mph
mph = float(input("What is your speed in miles per hour? "))
mps = 0.4474 * mph
#Calculamos la velocidad en mps y lo mostramos en pantalla
print("Your speed in meters per second is: ",round(mps,2))