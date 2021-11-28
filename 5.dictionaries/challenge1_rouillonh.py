#Importamos la libreriarandom para usarlo luego
import random
#Definimos el dictionary con las palabras y sus respectivos sinónimos
thesarurus = {
    "hot":['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
    "cold":['chilly', 'cool', 'freezing', 'frigid', 'polar'],
    "happy":['content', 'cheery', 'merry', 'jovial', 'jocular'],
    "sad":['unhappy', 'downcast', 'miserable', 'glum', 'melancholy']
}
print("\tWelcome to the Thesaurus App!")
print("\nChoose a word from the thesaurus and I will give you a synonym.")
print("\nHere are the words in the thesaurus:")
#Le pedimos al usuario que palabra va escoger para imprimir un sinónimo aleatorio de esa palabra
for i in thesarurus.keys():
    print("\t-",i)
choice = input("\nWhat word would you like a synonym for: ")
x = random.randint(1,5)
if choice in thesarurus:
    print("A synonym for ",choice," is ",thesarurus[choice][x])
#Si esa palabra no se encuentra en el diccionario se imprime un aviso
else:
    print("The word entered does not exist")
c = input("\nWould you like to see the whole thesaurus (yes/no) ").lower()
#Ahora le preguntamos si quiere ver el contenido del diccionario
if c == 'yes':
    for clave in thesarurus:
        print("\n",clave.capitalize()," synonyms are:")
        for i in range(5):
            print("\t-",thesarurus[clave][i])
if c =='no':
    print("I hope you enjoyed the program. Thank you!")
