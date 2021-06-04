"""
Ejercicio de como estuvo tu dia
"""
bandera=True

while bandera:
    nivel = int( input("Califica tu dia del 1 al 10 :") )

    if nivel>=1 and nivel<=10:
        print("tu dia estuvo :",nivel)
        bandera=False
    else:
        print("por favor selecciona un numero del 1 al 10")

