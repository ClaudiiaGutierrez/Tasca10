def llegir_llista():
    a = 1
    l=[]
    while a!='a':
        a=input("Introdueix un número diferent a 'a': ")
        if a !='a':
            l.append(int(a))
        else:
            return l

a = llegir_llista()
b = llegir_llista()
c =[]
for i in range(len(a)) :
    c.append(a[i]*b[i])
print("La multiplcació de la llista {} per la llista és {}".format(a,b,c))


"""
a=int(input("Introdueixi el primer valor: "))
b=int(input("Introdueixi el segon valor: "))
if a >= b:
    print("  {} és major o igual que {}".format(ab))
else:
      print(" {} és menor que {}".format(a,b))



a[]
for m in range(3):
    a.apped(int(input("Introdueix per número: ")))
print(a)
"""


""" a=[]
f = int(input("Introdueixi el tamany de la llista: "))
for m in range(f):
    a.append(int(input("Introdueix per número: ")))
print(a) """
