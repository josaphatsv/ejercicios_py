"""Ejercicio de funciones """
#como declarar un funcion en python
def mi_funcion():
    print("Saludos desde mi primera Funcion con python")

#como llamara una funcion en python
mi_funcion()

#funcion con parametros
def hola_mundo(nombre,apellido):
    print(f"Hola {nombre} {apellido} estas dentro de mi funcion")

#llamar la funcion pasando parametros
hola_mundo("Josaphat","Lopez")
hola_mundo("Cecilia","Flores")

#funcion con un return
def sumar2(a,b):
    return a + b
resultado = sumar2(5,3)
print(f'El resultado es : {resultado}')

def suma(a=0,b=0):
    return a+b
print(f'El resultado es : {suma(2,8)}')
#ejercicio con tupla
def sumar(*arg):
    total=0
    for numero in arg:
        total+=numero
    return total


print(f'la suma total es:{sumar(5,8,6,9,10)}')
#ejercicio con tuplas
def multiplicar(*args):
    resultado=1
    for numero in args:
        resultado*=numero
    return resultado
print(f'La multiplicacion total es: {multiplicar(2,2,2,2)}')

#funcion con diccionario
def deficion_nombres(**nombres):

    for llave, valor in nombres.items():
        print(f"{llave} : {valor}")


dict={
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS':'Database Management System'
}
#funcion que recibe un diccionario 
deficion_nombres(**dict)