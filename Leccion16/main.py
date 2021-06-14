"""Ejercicio con diccionarios
"""
#declarar un diccionario
diccionario={
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS':'Database Management System'
}
#imprimir un diccionario
print(diccionario)
#saber el largo de un diccionario
print(len(diccionario))
#acceder a un elemento del diccionario
print(diccionario['IDE'])
#otra forma de acceder a un elemento
print(diccionario.get('OOP'))
#modificar un elemento del diccionario
diccionario['IDE']='Integrated-Development-Environment'
print(diccionario)
#recorrer los elementos de un diccionario
for termino, valor in diccionario.items():
    print(termino,valor)

for termino in diccionario.keys():
    print(termino)
for valor in diccionario.values():
    print(valor)
#comprobando si existencia de algun elemento de un diccionario
print('IDE' in diccionario)

#agregar un elemento al diccionario
diccionario['PK']='Primary key'
print(diccionario)
#eliminar un elemento de un diccionarion
diccionario.pop('PK')
print(diccionario)
#limpiar un diccionario
diccionario.clear()
print(diccionario)