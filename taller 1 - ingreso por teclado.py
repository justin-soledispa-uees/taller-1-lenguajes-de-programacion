suma = 0
contador = 1

while contador <= 10:
    valor = float(input(f"Ingrese el valor {contador}: "))
    suma += valor
    contador += 1 

promedio = suma / 10
print(f"Suma: {suma}, Promedio: {promedio}")