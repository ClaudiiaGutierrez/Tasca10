def super_posicio(c):
    a=[3, 5, 6, 7, 9,]
    b=[7, 3, 8, 1, 4,]
    c= c.lower()
    if b in a:
        return True
    else:
        return False

#Programa Principal
x=input("Introdueix un numero de la llista: ")
if  super_posicio(x):
    print(("El número {} no esta en comú amb s'altre lista").format(x))
else:
    print((" El número {} ésta en comù amb s'altre llista ").format(x))  