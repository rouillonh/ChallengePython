#Importamos la libreria random para que escoja un valor aleatorio
import random
print("\tWelcome to a game of Rock, Paper, Scissors")
n = int(input("\nHow many rounds would you like to play: "))
player = 0
pc = 0
#Creamos una variable donde se guardara la funcion choice de random para que escoja entre piedra, papel o tijera
x = random.choice(["rock","paper","scissors"])
#Empezamos el bucle for para que asi se jueguen la cantidad de rounds que el usuario escogió
for i in range(1,n+1):
    print("\nRound ",i)
    print("Player: ",player,"\tComputer: ",pc)
    m = input("Time to pick...rock, paper, scissors: ")
    print("\tComputer: ",x)
    print("\tPlayer: ",m)
    if m == 'paper' and x == 'rock':
        player+=1
        print("\tPaper covers rock!")
        print("\tYou win round ",i)
    elif m == 'paper' and x== 'scissors':
        pc +=1
        print("\tScissors cuts paper!")
        print("\tComputer win round ",i)
    elif m == 'rock' and x== 'scissors':
        player +=1
        print("\tRock breaks scissors!")
        print("\tYou win round ",i)
    elif m == 'rock' and x == 'paper':
        pc +=1
        print("\tPaper covers rock!")
        print("\tComputer win round ",i)
    elif m == 'scissors' and x == 'paper':
        player +=1
        print("\tScissors cuts paper!")
        print("\tYou win round ",i)
    elif m == 'scissors' and x== 'rock':
        pc +=1
        print("\tRock breaks scissors!")
        print("\tComputer win round ",i)
    elif m == x:
        player = player
        pc = pc
        print("\tIt is a tie, how boring!")
        print("\tThis round was a tie.")
#Despues de jugarse una reñida competencia, se muestran los resultados y asi quien es el ganador
print("\nFinal Game Results")
print("\tRound played: ",n)
print("\tPlayer score: ",player)
print("\tComputer score: ",pc)
if player > pc:
    print("\tWINNER: PLAYER!!!")
elif pc > player:
    print("\tWINNER: COMPUTER :-(")
elif pc == player:
    print("\tWINNER: nobody, it's a tie")


