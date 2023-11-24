
#a = [3, (1,3), [4, 5, 6], 7, "hola", '0', 0, 1]
a='d'
if a == 'b':
    print("a és b")
elif a == 'c':
    print("a és c")
elif a == 'd':
    print("a és d")
elif a == 'e':
    print("a ès e")
else:
    print("a no val res")


match a:
   case 'b': 
        print("a és b")
   case 'c':
         print("a és c")
   case 'd':
        print("a és d")
   case 'e':
        print("a ès e")
   case other:
        print("a no val res")


"""
a = [3, (1,3), [4, 5, 6], 7, "hola", '0', 0, 1]
if 'a' in a:
    print("a és dins la llista {}".format(a))
elif 'holas' in a:
    print("AIxò s'executa si és certa la condició")
elif '0b' in a:
    print("b ès dins {}".format(a))
else:
    print("Dins a hi ha {}".format(a))
"""