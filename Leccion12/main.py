"""Ejercicios de ciclos """

#Ciclo while

num=5
while num>0:
    print(num)
    num-=1
else:
    print("fin del ciclo while")

#Ciclo for
cadena="Hola"

for letra in cadena:
    print(letra)
else :
    print("fin del ciclo for")

palabra="holanda"

for letra in palabra:
    if letra=="a":
        print(f"fin del ciclo se encontro la letra {letra}")
        break
else:
    print("Fin de ciclo con break")

#forma de ocupar continue

for i in range(6):
    if i%2!=0:
        continue
    print(f"Valor : {i}")

