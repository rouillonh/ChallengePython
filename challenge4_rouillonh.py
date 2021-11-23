import math
print("\tWelcome to the Right Triangle Solver App")
#Pedimos los valores de los catetos
c1 = float(input("\nWhat is the first leg of the triangle: "))
c2 = float(input("What is the second leg of the triangle: "))
#Calculamos la hipotenusa y el área
h = math.sqrt((c1**2)+(c2**2))
area = c1*c2/2
#Imprimimos los valores
print("\nFor a triangle with legs of ",c1," and ",c2," the hypotenuse is ",round(h,4))
print("\nFor a triangle with legs of ",c1," and ",c2," the area is ",round(area,4))