#Leer una cadena y devolver el numero de palabras de dicha cadena

ab= input("dijite la cadena")

# es para que no se confunda las mayuculas 
ab= ab.lower()

#es para quitar el espasio entre palabras
ac= ab.split(" ")
ad= 0
for ac in ac :
    ad+=1
print(f"numero de palabras -{ad}-")
