#Funciò que llegeix una llista
def llegir_llista():
	a=[]
	c="a"
	while c!=".":
		c=input("Introdueixi un element de la llista i punt (.) per acabar: ")
		if c!=".":
			a.append(c)
	return a
#Funció que elimina capicua donada una llista, elimina el primer i el darrer element
#Retorna una nova llista sense es 2 elements
def eliminar_capicua(a):
	b=[]
	if len(a)>2:
		b=a[1:-1]
	return b
#Programa Principal
x = llegir_llista()
y = eliminar_capicua(x)
print("La llista original {} s'ha transformat en la llista {}".format(x,y))

    
        		
		