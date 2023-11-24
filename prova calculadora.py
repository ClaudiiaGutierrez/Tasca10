# Funcions de canvis de base
# De decimal a binari, octal i hexadecimal
def dectobin(numero):
    # Prec: numero sigui un enter
    # Post: Escriu el valor de l'enter en binari
   return bin(numero)
def dectooct(numero):
    # Prec: numero sigui un enter
    # Post: Escriu el valor de l'enter en binari
   return bin(numero)
def dectohex(numero):
    # Prec: numero sigui un enter
    # Post: Escriu el valor de l'enter en binari
   return hex(numero)
# De binari a octal, decimal, hexadecimal
def bintooct(numero):
    # Prec: numero sigui una cadena de caracters
    # Post: escriu el número en octal
    a=int(numero,2)
    return dectooct(a)
def bintodec(numero):
    # Prec: numero sigui una cadena de caracters i en binari
    # Post: escriu el número en decimal
    a=int(numero,2)
    return a
def bintohex(numero):
    # Prec: numero sigui una cadena de caracters i en binari
    # Post: escriu el número en decimal
    a=int(numero,2)
    return dectohex(a)   


#Programa principal
x = int(input("Introdueix un número en decimal: "))
print(dectobin(x))

#