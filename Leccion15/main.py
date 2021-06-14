"""
Ejercicio de un elemento Set

la diferencia con los elementos lista o tupla
es que Set no mantiene un orden y tampoco permite almacenar elementos duplicados
no es posible modificar los elementos almacenados de un set, pero si se puede agregar mas elementos
"""
#definir un elemento set
planetas={'Marte','Jupiter','Venus','Sol'}
#podemos observar que no lo imprime en orden
print(planetas)
#para saber el largo del Set
print(len(planetas))
#revisar si si tiene un elemento esta presente
print('Marte' in planetas)
#agregrar un elemento a set
planetas.add('Tierra')
print(planetas)
#no se puede duplicar elementos
planetas.add('Sol')
print(planetas)
#eliminar un elemento pero si no lo encuentra arroja error
planetas.remove('Sol')
print(planetas)
#Elimina un elemento sin arrojar un Error
planetas.discard('Sol')
print(planetas)
#Limpiar un element Set
planetas.clear()
print(planetas)
#Eliminar el elemento como tal
del planetas
print(planetas)