
def draw_board(lista):
    print("------------------")
    print("|| " ,lista[0]," || ",lista[1]," || ",lista[2]," ||")
    print("------------------")
    print("|| " ,lista[3]," || ",lista[4]," || ",lista[5]," ||")
    print("------------------")
    print("|| " ,lista[6]," || ",lista[7]," || ",lista[8]," ||")
    print("------------------")
def get_player_input(a,lista):
    ban = True 
    while ban:
        print(a,end="")
        pos = int(input(": Where would you like to place your piece (1 - 9): "))
        if pos >= 1 and pos <= 9:
            if  lista[pos-1] == "X" or lista[pos-1] == "O":
                print("That spot has already been chosen. Try again.")
                continue
            
            else:
                return pos
            
        if pos <= 1 or pos >= 9 :
            print("That is not a spot on the board. Try again.")
            continue
def place_char_on_board(a,pos,lista):
    lista[pos-1] = a
def is_winner(lista,a):
    if lista[0] == a and lista[1] == a and lista[2] ==a:
        
        return True
    elif lista[3] == a and lista[4] == a and lista[5] ==a:
        
        return True
    elif lista[6] == a and lista[7] == a and lista[8] ==a:
        
        return True
    elif lista[0] == a and lista[3] == a and lista[6] ==a:
        
        return True
    elif lista[1] == a and lista[4] == a and lista[7] ==a:
        
        return True
    elif lista[2] == a and lista[5] == a and lista[8] ==a:
        
        return True
    elif lista[0] == a and lista[4] == a and lista[8] ==a:
        
        return True
    elif lista[2] == a and lista[4] == a and lista[6] ==a:
        
        return True
    return False
def full_board_check(lista):
    return len([i for i in lista if i == '_']) == 1
player1="X"
player2="O"
c_list = ['_']*9
n_list = ["1","2","3","4","5","6","7","8","9"]
draw_board(n_list)
print("\n")
draw_board(c_list)
band = True
while band:
    c = get_player_input(player1,c_list)
    print("\n")
    place_char_on_board(player1,c,c_list)
    draw_board(n_list)
    print("\n")
    draw_board(c_list)
    if is_winner(c_list,player1):
        print("The player 1 is the winner!")

        break
    if "_" not in c_list:
        print("is a tie!")
        break
    n = get_player_input(player2,c_list)
    print("\n")
    place_char_on_board(player2,n,c_list)
    print("\n")
    draw_board(c_list)
    if is_winner(c_list,player2):
        print("the player 2 is the winner!")
        break
    if "_" not in c_list:
        print("Is a tie!")
        break





            





