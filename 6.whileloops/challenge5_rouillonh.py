import random
print("\t--------------------Power-Ball Simulator--------------------")
#Pedimos el rango de numeros para la cantidad de bolas blancas
white_balls = int(input("How many white-balls to draw from for the 5 winning numbers (Normally 69):"))
if white_balls <= 5:
    white_balls = 5
#Lo mismo para las bolas rojas
red_balls = int(input("How many red-balls to draw from for the Power-Ball (Normally 26): "))
if red_balls <= 1:
    red_balls = 1
odd = 1
#Aqui creamos la variable para hallar la probabilidad de que el usuario acierte
for i in range(5):
    odd *= white_balls-i
odd = odd *red_balls/120
print("You have a 1 in ",odd," chance of winning this lottery.")
ticket_interval = int(input("Purchase tickets in what interval: "))
print("\n---------Welcome to the Power-Ball-----------")
winning_number = []
#Creamos la lista winning_number para alamacenar la combinacion ganadora
while len(winning_number) != 5:
    x = random.randint(1,white_balls)
    if x not in winning_number:
        winning_number.append(x)  
    winning_number = sorted(winning_number)
y = random.randint(1,red_balls)
winning_number.append(y)
wn = ""
for i in winning_number:
    wn += " "+str(i)

print("\nTonight's winning numbers are: ",wn)
print("Press 'Enter' to begin purchasing tickets!!!",end="")
input()
tickets_purchased = 0
flag = True
#Aqui creamos el bucle para asi poner la cantidad de combinaciones que tiene el usuario
while flag:
    nums = []
    while len(nums) != 5:
        m = random.randint(1,white_balls)
        if m not in nums:
            nums.append(m)
        nums = sorted(nums)
    n = random.randint(1,red_balls)
    nums.append(n)
    tickets_purchased += 1
    print(nums)
    if tickets_purchased%ticket_interval==0:            
        if nums != winning_number:
            print(tickets_purchased," tickets purchased so far with no winners...")
            #Al momento de no tener la combinacion , le preguntamos si desea continuar
            c = input("\nKeep purchasing tickets (y/n): ").lower()
            if c == "y":           
                flag = True
            elif c == "n":
                print("\nYou bought ",tickets_purchased, " tickets and still lost!")
                print("Better luck for next")
                flag = False
    elif tickets_purchased%ticket_interval != 0:
        nums2 = ""
        if nums == winning_number:
            for i in nums:
                nums2 += " " + str(i)

            print("Winning ticket numbers: ",nums2)
            print("Purchased a total of ",tickets_purchased," tickets.")     
            flag = False
    

        
    
    
    
    

