#Crear una lista_uno y adicione elementos en ella hasta que el usuario elija terminar.

#Una vez terminada, crear una segunda lista_dos, en ella llene los valores de lista_uno de forma descentente.

from contextlib import nullcontext

lista1=[]
lista2=[]

def add():
  x=input("DIgite un valor para la lista: ")
  lista1.append(x)
  print("[",lista1,"]")

n=True
while True:

  add()

  n=input("Desea continuar agrgando elementos a la lista? (y/n):")
  if n== 'n' or n=='N':
    break

lista2 = lista1
reverse = lista2[::-1]
print("[",reverse,"]")