#Definició de la funció
def major(a):
    if a>18:
        print("És major d'edat")
    elif a<18:
        print("Ès menor d'edat")
    else:
        print("Té 18 anys")

#Programa principal
x = int(input("Introdueixi la seva edat: "))
major(x)