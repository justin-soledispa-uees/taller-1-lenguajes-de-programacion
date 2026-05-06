import time

inicio = time.time()
suma = 0
contador = 1

while contador <= 10:
    valor = int(input(f"Ingrese el valor {contador}: "))
    suma += valor
    contador += 1 

promedio = suma / 10
print(f"Suma: {suma}, Promedio: {promedio}")
fin = time.time()

total = fin - inicio
print(f"\nTiempo {total:.3f} segundos ")