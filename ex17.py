def sumar_llista(a):
		suma = 0
		for i in a:
			suma += i
		return suma
def multiplicar_llista(a):
		multiplicar = 1
		for i in a:
			multiplicar *=i
		return multiplicar
# Programa Principal
x = [4, 7, 9, 3]
print("La suma de tots els elements de la llista és: ", sumar_llista(x))
print("La multiplicació de tots els elements de la llista és: ", multiplicar_llista(x))
