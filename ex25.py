def paraula_mes_gran(a):
	sorted(a,key=lambda a:len(a))
	return a[len(a)-1]

# Programa principal
x = ["hola", "Adeu", "Si", "Sopa", "Menorca", "Les platges de Menorca son molt polides"]
print("La paraula més llarga és: ", paraula_mes_gran(x))
