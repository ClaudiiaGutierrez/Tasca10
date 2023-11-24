def menu_principal():
    print("""
      Menú principal:
      1. Calculadora enters
      2. Calculadora reals
      3. Sortir
      """)
    a = int(input("Elegeixi una opció: "))
    return a
def calculadora_enters():
    print("Hem passat per la calculadora d'enters")

def calculadora_reals():
    print("Hem passat per la calculadora de reals")
       
#Programa principal
a  = 1
while a>0:
    a = menu_principal()
    match a:
      case 1:
        calculadora_enters()
      case 2:
        calculadora_reals()
      case 3:
        a = -1
      case other:
        print("Opció no vàlida!")
        a =int("Elegeix una opció: ")

def calculadora_enters():
   op = 1
   while op<0:
      print("""
        Menú principal
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        5. Sortir
       """)
      op = int(input("Elegeixi una opció: "))
      match op:
         case 1: # Sumar
            x = int(input("Introdueixi el primer número: "))
            y = int(input("Introdueixi el segon número: "))
            print("{} + {} = {}".format(x, y, x+y))
         case 2: # Restar
            x = int(input("Introdueixi el primer número: "))
            y = int(input("Introdueixi el segon número: "))
            print("{} - {} = {}".format(x, y, x-y))
         case 3: # Multiplicar
            x = int(input("Introdueixi el primer número: "))
            y = int(input("Introdueixi el segon número: "))
            print("{} * {} = {}".format(x, y, x*y))
         case 4: # Dividir
            x = int(input("Introdueixi el primer número: "))
            y = int(input("Introdueixi el segon número: "))
            print("{} / {} = {}".format(x, y, x/y))
         case 5: # Sortir 
              print("Adéu, ja tornaràs a la calculadora inicial \n\n")
              op=1
def calculadora_reals():
    z = 1
    while z>0:
        print("""
            Menu_principal:
                 1. Sumar
                 2. Resta
                 3. Divisió
                 4. Multiplicar
                 5. Sortida
                 """)
        z = int(input("Elegeix una opció: "))
        match z:
            case 1:
                a = float(input("Introdueix un nombre: "))
                b = float(input("Introdueix el segon nombre per sumar: "))
                print("La suma de {} + {} = {}".format(a,b,a+b))

            case 2:
                a = float(input("Introdueix un nombre: "))
                b = float(input("Introdueix el segon nombre per restar: "))
                print("La resta de {} - {} = {}".format(a,b,a-b))

            case 3:
                a = float(input("Introdueix un nombre: "))
                b = float(input("Introdueix el segon nombre per multiplicar: "))
                print("La multiplicació de {} * {} = {}".format(a,b,a*b))

            case 4:
                a = float(input("Introdueix un nombre: "))
                b = float(input("Introdueix el segon nombre per dividir: "))
                print("La divisió de {} / {} = {}".format(a,b,a/b))
            case 5:
                z =-1
            
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
# Hexadecimal a binari, octal i decimal
def hextonum(hex): # Aquesta funció passa quasevol hexadecimal a un numero
    pnum = {
        "f": 15,
        "e": 14,
        "d": 13,
        "c": 12,
        "b": 11,
        "a": 10
     }
    if hex in pnum:
        return pnum[hex]
    else:
        return int(hex)
def hextodec2(hex):
    hex = hex.lower()
    hex = hex[ : : -1]
    decimal = 0
    posicio = 0
    for digit in hex:
        valor = hextonum(digit)
        elevat = 16 ** posicio
        pnum = elevat * valor
        decimal += pnum
        posicio +=1
    return decimal
def hextobin(numero):
    a=int(numero,16)
    return dectobin(a)
def hextooct(numero):
    a=int(numero,16)
    return dectooct(a)
def hextodec(numero):
    a = int(hextodec2(numero))
    return a
   

def canvi_de_base():
    while op>0:
        print("""
            Menu_principal:
                 1. Donat un binari ho passem a tota la resta
                 2. Donat a un octal el passam a tota la resta
                 3. Donat un decimal ho passem a tota la resga
                 4. Donat un hexadecimal ho passem a tota la resta
                 5. Sortir
                 """)
        op = int(input("ELegeixi una opció: "))
        match op:
            case 1: # Binari to
              b = input("Introdueixi el número binari: ")
              o = bintooct(b)
              d = bintodec(b)
              h = bintohex(b)
              print("El número binari {} és: \n oct -> {} \n hex -> {}".format(b,o,d,h))
            case 2: # Octal to
              o = input("Introdueixi el número octal: ")
              o = octtooct(b)
              d = octtodec(b)
              h = octtohex(b)
              print("El número octal {} és: \n bin -> {} \n hex -> {}".format(b,o,d,h))
            case 3: # Decimal to
              d = input("Introdueixi el número Decimal: ")
              o = dectooct(b)
              b = dectobin(b)
              h = dectohex(b)
              print("El número decimal {} és: \n bin -> {} \n hex -> {}".format(b,o,d,h))
            case 4: #Hexadecimal to
              h = input("Introdueixi el número Hexadecimal: ")
              o = hextooct(b)
              b = hextobin(b)
              h = hextohex(b)
              print("El número hexadecimal {} és: \n bin -> {} \n hex -> {}".format(b,o,d,h))
            case 5: #Sortir
              print("Adéu, tornaràs a la calculadora inicial \n\n")
              op=-1 

