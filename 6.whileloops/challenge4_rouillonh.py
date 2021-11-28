import random
print("\nWelcome to the Guess My Word App")
game_dict = {
    "deportes":["futbol","voley","baloncesto","golf","tenis","atletismo"],
    "colores":["rojo","verde","azul","amarillo","blanco","negro"],
    "animales":["perro","gato","hamster","conejo","caballo","jirafa"],
    "frutas":["manzana","banana","mango","naranja","fresa","mandarina"]
}
game_keys = []
for i in game_dict.keys():
    game_keys.append(i)
band = True
while band:
    categoria_juego = game_keys[random.randint(0,3)]
    game_word = game_dict[categoria_juego][random.randint(0,5)]
    blank_word = []
    for i in range(len(game_word)):
        blank_word.append("-")
    blank_word2 = "".join(blank_word)
    guess = ""
    guess_count = 0
    print("Guess a ",len(game_word) ," letter word from the following category:",categoria_juego.capitalize())
    print(blank_word2)
    guess = input("\nEnter your guess: ")
    guess_count += 1
        
    if guess != game_word:          
        letter_count = random.randint(0,len(blank_word))
        blank_word[letter_count] = game_word[letter_count]         
        print("That is not correct. Let us reveal a letter to help you!")
        print(blank_word2)
        continue
    elif guess == game_word:
    
        print("Correct! You guessed the word in ",guess_count ," guesses.")
        break
            
            
    c = input("Would you like to play again (y/n): ").lower()
    if c == "y":
        continue
    elif c == "n":
        print("\nThank you for playing our game.")
        band = False


