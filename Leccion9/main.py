"""
Validacion con sentencias if,elif y else
"""
numero=int(input("Proporcione un valor entre 1 y 3: "))
numeroTexto=''
if numero==1:
    numeroTexto="Numero uno"
elif numero==2:
    numeroTexto="Numero dos"
elif numero==3:
    numeroTexto="Numero tres"
else:
    numeroTexto="valor fuera del rango"

print(f"""
        El Numero proporcionado es:3
            {numero} : {numeroTexto} 
        """)

#Operadores ternarios

print("valor esta dentro del rango") if numero>0 and numero<=3 else print("valor fuera del rango")