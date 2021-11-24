print("\tBienvenido al Grade Sorter App\n")
#Primero preguntamos al usuario sus 4 grados
primero = int(input("¿Cual es tu primer grado?(0-100): "))
segundo = int(input("¿Cual es tu segundo grado?(0-100): "))
tercero = int(input("¿Cual es tu terce grado?(0-100): "))
cuarto = int(input("¿Cual es tu cuarto grado?(0-100): "))
#Luego, los añadimos a una nueva lista
a = []
a.append(primero)
a.append(segundo) 
a.append(tercero)
a.append(cuarto)
#Ordenamos la lista de manera numérica
b = sorted(list(a))[ : :-1]
print("Tus grados son: ",list(a))
print("Tus grados en orden descendente son: ",b)
#Eliminamos los grados de menor valor
print("\nLos dos últimos grados que ahora serán eliminados son: ")
print("Eliminar grado: ",  b.pop(3))
print("Elimnar grado: ", b.pop(2))
print("\n")
print("Tus grados restantes son: ",b[0:2])
#Finalmente, tenemos el valor más alto de la lista de grados
print("¡Buen trabajo! Tu grado más alto es: ",b[0])