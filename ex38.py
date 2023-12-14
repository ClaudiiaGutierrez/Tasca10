#Programa Principal
x = float(input("Introdueix la quantitat sol·licitada (50000 i 80000) euros: "))
y = float(input("Introdueix l'interés (0.5 i 13) percentatge: "))
z = int(input("Introdueix el número d'anys: "))
cfinal = x * (1 + y/100)**z
print("El capital {}€ a un interés del {}% a {} anys resulta que pagarem {:.2f}€".format(x, y, z, cfinal))
