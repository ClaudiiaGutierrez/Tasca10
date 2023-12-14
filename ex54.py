#Funció que sumi tots els números entre dos números donats
def sumar(a,b):
   suma=0
   if a>b:
      for i in range(b,a+1,1):
          suma+=i
   elif b>a:
   	for i in range(a,b+1,1):
           suma+=i
   else:
       suma=0
       


#Programa Principal
a = int (input("Introdueix el primer número: "))
b = int (input("Introdueix el segon número: "))
c = sumar(a,b)
print("La suma dels números entre {} i {} és {}".format(a, b, c))

      

      

