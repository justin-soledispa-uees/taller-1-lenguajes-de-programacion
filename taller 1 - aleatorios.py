import random as rd

pares = 0
impares = 0

for i in range(500):
    num = rd.randint(50, 100)
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Total pares : {pares}")
print(f"Total impares : {impares}")