print("\tWelcome to the Temperature Coonversio App")
#Pedimos el valor de la temperatura en fahrenheit
temp = float(input("\nWhat is the given temperature in degrees Fahrenheit: "))
celsius = (temp-32)*5/9
kelvin = celsius + 273.15
#Convertimos a celsius e imprimimos los valores
print("\nDegrees Fahrenheit: \t",temp)
print("Degrees Celsius: \t",round(celsius,4))
print("Degrees Kelvin: \t",round(kelvin,4))