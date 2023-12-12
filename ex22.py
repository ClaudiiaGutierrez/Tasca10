def crear_repetits(a,b):
	c = b*int(a)
	return c

def crear_punts(a):
	for e in a:
            c=crear_repetits(int(e),'.')
            print(c)

#Programa Principal
a = input("Escriu una llista numèrica d'elements: ")
crear_punts([2,3,4])