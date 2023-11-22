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
        return a
def calculadora_enters():
   op = 1
   while op<0:
      print("""
        Menú enters
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
  