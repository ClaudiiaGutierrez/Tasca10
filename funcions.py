def canvi(l, m,n):
    l=int(input("Introdueixi el nou valor per aquesta variable : "))
    print("1){}{} \n {}".format(l, m, n,))
    l='Adéu'
    m='Joan'
    n='Que vagi bé'
    print("2) {}{} \n {}".format(l, m, n))
# Programa principal
a="Hola,"
b="Ramis."
c="Com estas"
a=1001
print("EL valor de la variable abans de canviar és: {}{} \n {}".format(a, b, c))
canvi(a, b, c)
print("El valor de la variable després de canviar és: {}{} \n {}".format(a, b, c))
    
"""
def canvi(l):
    x = input ("Introdueix el valor a inserir el conjunt: :")
    l.add(x)
# Programa principal
a =(3, 5, 7, 9, 10)
print("EL valor del conjunt abans de canviar és: {}".format(a))
canvi(a)
print("EL valor del conjunts després de canviar és: {}".format(a))


def canvi(l):
   l=(1,2,6, 8)
# Programa principal
a =(3, 5, 7, 9, 10)
print("EL valor de la tupla abans de canviar és: {}".format(a))
canvi(a)
print("El valor de la tupla després de canviar és: {}".format(a))



def canvi(l):
    #Funció que demana quina posició vols modificar
    x = input ("Introdueix la posició a modificar:")
    l[x]=input ("Introdueix el valor a inserir: ")
# Programa principal
#Funció amb tuples, cadena de caracters i llista
a =[3, 4, 5, 6, 7, 8, 'a', (1,2),[3,4],10]
print("EL valor de la llista abans de canviar és: {}".format(a))
#Funció que canvia la llista
canvi(a)
#Funció que mostra com a cambiat la llista modificada
print("El valor de la llista després de canviar és: {}".format(a))
"""
"""
def intercanvi(a,b):
    return b,a
x='a'
y='b'
print("El valor d'x és {} i el d'y és {}".format(x,y))
x,y = intercanvi(x,y)
print("Despres de l'intercanvi, el valor d'x és {} i el d'y és {}".format(x,y))



def major(x,y):
 
 x = int(input("{} és major que {}"))
 y = int(input("{} és menor que {}"))

"""