def es_palindrom(c):
    p=("ara")
    b=c.lower()
    if b in p:
        return True
    else:
        return False 


#Programa Principal
z=input("Introdueixi la paraula: ")
if es_palindrom(z):
    print(("{} ès palindrom").format(z))
else:
    print(("{} no es palindrom").format(z))

