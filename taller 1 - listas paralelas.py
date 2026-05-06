sucursales = ["S1", "S2", "S3", "S4", "S5","S6", "S7", "S8", "S9", "S10","S11", "S12", "S13", "S14", "S15","S16", "S17", "S18", "S19", "S20","S21", "S22", "S23", "S24", "S25"]

ventas = [15000.0, 28000.0, 3200.0, 1100.0, 4500.0,
    2100.0, 3000.0, 1800.0, 25600.0, 4188.0,
    12900.0, 3300.0, 27000.0, 1900.0, 36070.0,
    4800.0, 1400.0, 22050.0, 3100.0, 2600.0,
    1700.0, 3910.0, 24033.0, 1300.0, 4200.0]


suma_total = 0
for v in ventas:
    suma_total += v

promedio_ventas = suma_total / len(ventas)

print(f"Promedio general de ventas: ${promedio_ventas:.2f}")
print("Sucursales con ventas mayores al promedio:")


for i in range(len(ventas)):
    if ventas[i] > promedio_ventas:
        print(f" {sucursales[i]} con ${ventas[i]:.2f}")