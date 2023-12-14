#Funciò que cerca noms que comencen per la lletra a
def noms_que_comencen_per(llista,lletra):
	comptador = 0
	llnom= []
	for e in llista:
		if e[0]==lletra:
			llnom.append(e)
			comptador += 1
print("El número de noms que comencen per el caràcter {} són: {} i són: {}".format)
#Funció que llegeix una llista
def llegir_llista():
	b = []
	a = "a"
	while a != ".":
		a = input("Introdueixi el següent nom: ")
		if a!= ".":
			b.append(a)
		else:
			return b
	

    	
        	
        	
 
# Programa principal
noms = llegir_llista()
caracter = input("Introdueixi el caràcter que vols que comencin les paraules a cercar: ")
noms_que_comencen_per(noms,caracter)

