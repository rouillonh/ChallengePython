import random
print("\tWelcome to the Coin Toss App")
flip = int(input("How many times would you like me to flip the coin: "))
r = input("Would you like to see the result of each flip (y/n): ").lower()
x = []
head = 0
tail = 0
print("\nFlipping!\n")
if r.startswith('n'):
    for i in range(flip):
        tiro = random.randint(0,1)
        if tiro == 0:
            x.append("heads")
        elif tiro ==1:
            x.append("tails")
        if x.count("heads") == x.count("tails"):
            print("At ",x.count("heads")+x.count("tails")," flips, the number of heads and tails were equal at ",(x.count("heads")+x.count("tails"))/2,"each.")
    print("\nResults Of Flipping A Coin ",flip," Times:\n")
    print("Side\t\tCount\t\tPercentage")
    print("Heads\t\t",x.count("heads"),"/",flip,"\t",round(x.count("heads")/flip *100,2),"%")
    print("Tails\t\t",x.count("tails"),"/",flip,"\t",round(x.count("tails")/flip *100,2),"%")
if r.startswith('y'):
    for i in range(flip):
        tiro = random.randint(0,1)
        if tiro == 0:
            print("HEADS")
            x.append("heads")   
        elif tiro ==1:
            print("TAILS")
            x.append("tails")
        if x.count("heads") == x.count("tails"):
            print("At ",x.count("heads")+x.count("tails")," flips, the number of heads and tails were equal at ",(x.count("heads")+x.count("tails"))/2,"each.")
    print("\nResults Of Flipping A Coin ",flip," Times:\n")
    print("Side\t\tCount\t\tPercentage")
    print("Heads\t\t",x.count("heads"),"/",flip,"\t",round(x.count("heads")/flip *100,2),"%")
    print("Tails\t\t",x.count("tails"),"/",flip,"\t",round(x.count("tails")/flip *100,2),"%")
