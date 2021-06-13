"""Ejercicio de Listas"""

#Definimos una lista de tipo str
nombres=['Juan', 'Cecilia', 'Pedro', 'Maria', 'Pablo']
#imprimir la lista nombres
print(nombres)
#acceder a los elementos de una listar individual
print(nombres[0])
print(nombres[3])
#acceder a los elementos de una manera inversa
print(nombres[-1])
print(nombres[-5])
#imprimir un rango de elementos
print(nombres[0:3])
print(nombres[0:2])
#Desde el indice indicado hasta el final
print(nombres[2:])
#Cambiar un valor o sobre escribir en un indice
nombres[3]='Jorge'
print(nombres)
nombres[2]='Maria'
print(nombres)
#iterar una lista
for nombre in nombres:
    print(f'Su nombre es: {nombre}')
else:
    print("no existe mas nombres en la lista")

#saber cuantos elementos tiene nuestras lista
print(len(nombres))
#agregar un nuevo elemento a una lista
nombres.append('Santiago')
print(nombres)
#agrega un elemente a un numero de indice especifico
nombres.insert(3,'Pedro')
print(nombres)
#remover un elemento de una lista
nombres.remove('Jorge')
print(nombres)
#remover el ultimo elemento de una lista
nombres.pop()
print(nombres)
#eliminar un determinado indice
del nombres[2]
print(nombres)
#Borrar todos los elemetnos de una lista
nombres.clear()
print(nombres)
#borrar la lista
del nombres
print(nombres)