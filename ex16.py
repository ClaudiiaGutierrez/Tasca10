def es_vocal(c):
    p=['a', 'e', 'i', 'o', 'u']
    a= c.lower()
    if a in p:
        return True
    else:
        return False

#Programa Principal
s=input("Introdueix el caracter: ")
if es_vocal(s):
    print(("El caracter {} és vocal").format(s))
else:
    print((" El caracter {} és consonant").format(s))
