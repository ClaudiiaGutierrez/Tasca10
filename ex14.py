def gran(x, y, z):
    if x > z > y:
        return x
    elif z > y > x:
        return z  
    elif y > x > z:
        return y
    else:
        return print["Son iguals"]
       
#Programa principal
x= int(input("Introdueix es primer valor: "))
y= int(input("Introdueix es segon valor:  "))
z= int(input("Introdueix és tercer valor: "))
a= gran(x, y, z)
print("El major de {} {} {} és {}".format(x, y, z, a))





