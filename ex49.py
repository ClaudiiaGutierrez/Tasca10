from random import random
import random
def llista_30_elements():
    l = []
    for i in range(20):
        l.append(random.randint(1,100))
        return l
def hi_ha_duplicats(a):
    seen = set() 
    dupes = [x for x in a if x in seen or seen.add(x)]
    if len(dupes)>0:
         print("La llista {} te elements duplicats ".format(a,dupes))
    else:
         print("La llista {} no te elements duplicats".format(a,dupes))
def elimina_duplicats(a):
     b= list(set(a))
     return b
#Programa Principal
x = llista_30_elements()
hi_ha_duplicats(x)
y = elimina_duplicats(x)
y.sort()
print("Llavors, la llista sense elements duplicats és {}".format(y))






