def gran_llista(a):
	a.sort()
	return a[::-1]

# Programa principal
print("Es mès gran és: ")
a = [2, 50, 34, 35, 4, 6, 7, 10]
c = gran_llista(a)
print(c[0])
