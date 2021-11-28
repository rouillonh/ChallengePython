c = ''
#Empiezo el programa pidiendo la información al usuario
def get_info():
  print("\tBIENVENIDO AL PYTHON FIRST NATIONAL BANK")
  nombre = input("¿Cual es su nombre? ").title()
  ca = float(input("¿Con cuanto dinero le gustaría iniciar en la cuenta de ahorros? "))
  cc = float(input("¿Con cuanto dinero le gustaría iniciar en la cuenta de cheques? "))
  dic = {'Nombre':nombre,'Ahorros':ca,'Cheques':cc}
  print("\nInformación de la cuenta corriente:")
  for clave,valor in dic.items():
    if clave == 'Nombre':
      print(clave,": ",valor)
    elif clave == 'Ahorros' or clave == 'Cheques':
      print(clave,": $",valor)
  return dic
#Aquí cree esta variable dic2, como una variable universal ya que al momento de crear el diccionario en cada función el programa volvía a iniciar
dic2 = get_info()
#Creo las funciones para depósito
def make_deposit(): 
  try:
    cuenta = input("\n¿A qué cuenta te gustraía entrar?(Ahorros o Cheques) ")
    m = float(input("¿Cuánto dinero? "))
    if cuenta == 'ahorros':  
      dic2['Ahorros'] = dic2['Ahorros']+m
      print("Se han depositado $",m," en la cuenta de Ahorros de ",dic2['Nombre'])     
    elif cuenta == 'cheques':
      dic2['Cheques'] = dic2['Cheques']+m
      print("Se han depositado $",m," en la cuenta de Cheques de ",dic2['Nombre'])           
    for clave,valor in dic2.items():
      print(clave,": ",valor)
  except:
    print("La transacción no ha podido ser completada, ya que ha ingresado un valor inválido")
#Y para retiro
def make_withdrawal():
#En esta ocasión el código es más largo, debido a que cabe la posibilidad de al momento de pedir un valor a retirar, falte dinero
  try:
    cuenta = input("¿A qué cuenta te gustraía entrar?(Ahorros o Cheques) ")
    m = float(input("¿Cuánto dinero? "))
    if cuenta == 'ahorros':  
      if m > dic2['Ahorros']:
        print("\nLo sentimos, no se puede realizar la transacción ya que se produce un balance negativo")
      elif m <= dic2['Ahorros']:
        dic2['Ahorros'] = dic2['Ahorros']-m
        print("\nSe han retirado $",m," de la cuenta de Ahorros de ",dic2['Nombre'])     
    elif cuenta == 'cheques':
      if m > dic2['Cheques']:
        print("\nLo sentimos, no se puede realizar la transacción ya que se produce un balance negativo")
      elif m <= dic2['Cheques']:
        dic2['Cheques'] = dic2['Cheques']-m
        print("\nSe han retirado $",m," de la cuenta de Cheques de ",dic2['Nombre'])           
    for clave,valor in dic2.items():
      print(clave,": ",valor)
  except:
     print("La transacción no ha podido ser completada, ya que ingresó un valor inválido")
#Esta función es para terminar con el programa
def display_info():
  print("\n")
  for clave,valor in dic2.items():
    if clave == 'Nombre':
      print(clave,": ",valor)
    elif clave == 'Ahorros' or clave == 'Cheques':
      print(clave,": $",valor)
  print("¡Gracias! Que tenga un excelente día.")
#Y aca ya ejecuto todo junto
while True:
  try:
    op = input("\n¿Que operación le gustaría realizar?(Retiro/depósito) ")
    if op == 'retiro':
      make_withdrawal()
    elif op == 'deposito':
      make_deposit()
    c = input("¿Desea continuar con la transacción?(y/n)")
    if c == 'y':
      continue
    elif c == 'n':
      display_info()
      break
  except:
    print("\nLa transacción no ha podido ser completada")
