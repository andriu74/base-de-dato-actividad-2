#Leer una cadena y devolver cada palabra de la cadena y el nuemero de veces que se repite

ab= input("dijite la cadena")
ab= ab.lower()
ac= ab.split(" ")
ad={}
for ac in ac :
  if ac in ad:
    ad[ac]+= 1
  else:
    ad[ac]=1
for ac in ad:
   ba=ad[ac]
   print(f"la palabra- {ac}-se repite con una recuencia -{ba}-")