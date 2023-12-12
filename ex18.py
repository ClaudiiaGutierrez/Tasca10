def invertir(a):
	b = list(a)
	c = b[::-1]
	r = "".join(c)
	return r
# Programa principal
s="Soc de Menorca"
print("La cadena: ", "x", " girada és: ",invertir(s))
