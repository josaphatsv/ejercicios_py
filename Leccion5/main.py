"""Declaracion de variables"""
x = "Hola Mundo"
y = 12
z = True
a = 1.5
b = 3.141615
print(x)
"""Funcion que nos permite sabe que tipo de variable es """
print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))

# forma de concatenar variables
nombre = "Josaphat"
print("Hola " + nombre + ", como estas hoy " + nombre)
# segunda forma de concatenar
print("Hola ", nombre, ", como ests hoy ", nombre)
# error comun
numero1 = "1"
numero2 = "2"
print(numero1 + numero2)
# solucion
print(int(numero1) + int(numero2))

#variables bloeano
variable=3>2
print(variable)

if variable:
    print("Es verdadero")
else:
        print("Es falso")