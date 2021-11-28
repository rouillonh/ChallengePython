import random
def dice_sides():
    lados = int(input("How many sides would you like on your dice: "))
    return lados
def dice_number():
    rol = int(input("How many dice would you like to roll: "))
    return rol
def roll_dice(a,b):
    dados = []
    print("You rolled ",a," ",b ," sided dice.")
    for i in range(a):
        dados.append(random.randint(1,b))
    print("\n-----Results are as followed-----")
    for i in dados:
        print("\t",i)
    return dados
def sum_dice(c):
    suma = 0
    for i in c:
        suma += i
    print("The total value of your roll is ",suma)
def roll_again():
    x = input("Would you like to roll again (y/n): ").lower()
    if x == "y":
        return True
    if x == "n":
        print("\nThank you for using the Python Dice App.")
        return False
print("\tWelcome to the Python Dice App")
flag = True
while flag:
    a = dice_sides()
    b = dice_number()
    c = roll_dice(b,a)
    sum_dice(c)
    flag = roll_again()


