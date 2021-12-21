#Creamos una lista con los username
lista = ['favio','juancho','jaime','camilo']
print("\tWelcome to the Shipping Accounts Program")
#Pedimos el username y corroboramos si esta en la lista anterior
name = input("\nHello, what is your username: ").lower()
#Si está, entonces procedemos con la compra
if name in lista:
    print("\nHello ",name,". Welcome back to your account.")
    print("Current shipping prices are as follows:")
    print("Shipping orders 0 to 100:\t\t$5.10 each")
    print("Shipping orders 100 to 500:\t\t$5.00 each")
    print("Shipping orders 500 to 1000:\t\t$4.95 each")
    print("Shipping orders over 1000:\t\t$4.80 each")
    order = int(input("How many items would you like to ship: "))
    if order > 0 and order <= 100:
        print("To ship ",order," items it will cost you ",round(order*5.10,2) ," at $5.10 per item.")
    elif order >100 and order<=500:
        print("To ship ",order," items it will cost you ",round(order*5.00,2) ," at $5.00 per item.")
    elif order >500 and order <=1000:
        print("To ship ",order," items it will cost you ",round(order*4.95,2) ," at $4.95 per item.")
    elif order >1000:
        print("To ship ",order," items it will cost you ",round(order*4.80,2) ," at $4.80 per item.")
    else:
        print("Invalid value")
    x = input("Would you like to place this order (y/n): ").lower()
    if x.startswith('y'):
        print("Okay. Shipping your ", order ,"items.") 
    elif x.startswith('n'):
        print("Okay, no order is being placed at this time.")
#Si no está, no se procede
else:
    print("Sorry, you do not have an account with us. Goodbye.")

