#Damos la bienvenida y pedimos un valor
print("\tWelcome to the Binary/Hexadecimal Converter App")
num = int(input("\nCompute binary and hexadecimal values up to the following decimal number: "))
#Creamos una lista en blanco para despues llenarla con los valores decimales
lista = []
for i in range(0,num+1):
    lista.append(i)
print("Generating lists....complete!")
#Ahora creamos las listas para los valores en base binaria y hexadecimal
he = []
for i in range(0,num+1):
    he.append(hex(i))
bi = []
for i in range(0,num+1):
    bi.append(bin(i))
#Ahora de una porción de la lista de numeros decimales, mostramos sus respectivos valores en las otras bases
print("\nUsing slices, we will now show a portion of each list.")
a = int(input("What decimal number would you like to start at: "))
b = int(input("What decimal number would you like to stop at: "))
print("\nDecimal values from ",a,"to",b,":")
for i in range(lista[a],lista[b]+1):
    print(i,"\n")
print(f"\nBinary values from ",a," to ",b,":")
for i in range(a,b+1):
    print(bi[i],"\n")
print(f"\nHexadecimal values from ",a," to ",b,":")
for i in range(a,b+1):
    print(he[i],"\n")
#Finalmente, mostramos todos los valores en las tres bases
print("Press Enter to see all values from 1 to",num,".")
input("")
print("Decimal----Binary----Hexadecimal")
print("----------------------------------")
for i in range(0,10):     
        print(lista[i],"----",bi[i],"----",he[i])
