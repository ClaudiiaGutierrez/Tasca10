a  = 1
while a>0:
   print(""""
    Menú
    1. Mirar si es un número ès senar o parell
    2 Sortir
   """)     
   a = int(input("Seleccioni una opció: "))
   match a:
        case 1: #Si volem veure si un nùmero ès o no parell
            x = int(input("Escriure un número: ")) 
            if x % 2 == 0:
                 print("Ès parell")
            else:
                 print("Es senar(impar)")
        case 2:
             a =0