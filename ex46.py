#Funció que dona una llista ordenada
def  esta_ordenada(a):
    b = a.copy()
    c = a.copy()
    b.sort()
    c.sort(reverse=True)
    if a == b:
        print("La llista {} està ordenada ascendentment {}".format(a, b))
    elif a==c:
        print("La llista {} està ordenada descendentment {}".format(a, c))
    else:
        print("La llista {} no està ordenada {}".format(a, b))
#funciò que llegeix una llista
def llegir_llista():
    b = []
    a = "a"
    while a != ".":
        a = input("Introdueixi el següent número: ")
        if a != ".":
            b.append(int(a))
    else:
        return b
c =print("La llista {} es {}".format)

#Programa Principal
a = llegir_llista()
esta_ordenada(a)





