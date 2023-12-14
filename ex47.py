#Funció que diu si els elements estan duplicats o no
def hi_ha_duplicats(a):
    seen = set()
    dupes = [x for x in a if x in seen or seen.add(x)]
    if len(dupes)>0:
        print("La llista {} té elements duplicats {}".format(a,dupes))
    else:
        print("La llista {} no té elements duplicats {}".format(a,dupes))
#Funciò que llegeix una llista
def llegir_llista():
    a=[]
    c="a"
    while c!=".":
        c=input("Introdueixi un element de la llista i punt (.) per acabar: ")
        if c!=".":
            a.append(c)
    return a
#Programa Principal
a = llegir_llista()
hi_ha_duplicats(a)

