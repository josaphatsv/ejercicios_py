"""Ejercicio de una Tupla
    Diferencia entre una tupla y una lista es:
    Una Lista permite agregar, editar y eliminar un elemento
    Una tupla ya no podemos agregar modificar y Eliminarlos
    A esto se le conoce como inmutable
"""
#Definir una tupla
frutas=('Naranja','Platano','Sandia')

print(frutas)
#saber el largo de una tupla
print(len(frutas))
#acceder a un elemento de una tupla
print(frutas[0])
#navegacion inversa
print(frutas[-1])
#acceder a un rango
print(frutas[0:2])
#recorrer el elemento tupla
for fruta in frutas:
    print(fruta, end=' ')
#como modificar una tupla convirtiendo a una lista y volver colocar tupla
frutasListas=list(frutas)
frutasListas[0]='Pera'
frutas=tuple(frutasListas)
print('\n',frutas)
#eliminar una tupla completa
del frutas
print(frutas)
