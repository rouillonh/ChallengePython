print("\tWelcome to the Multiplication/Exponent Table App")
name = input("\nWhat is your name? ").capitalize()
num = float(input("What number would you like to work with: "))
print("\nMultiplication Table for ",num,"\n")
for i in range(1,11):
    print(i,"*",num,"=",round(i*num,4))
print("\nExponent Table for ",num,"\n")
for i in range(1,11):
    print(num,"**",i,"=",round(num**i,4))

print(name," Math is cool!")
print("\t",name.lower()," math is cool!")
print("\t\t",name.title()," Math Is Cool!")
print("\t\t\t",name.upper()," MATH IS COOL!")