alturas = []

for i in range(5):
    altura = float(input(f"Ingrese la altura de la persona {i + 1} (en cm): "))
    alturas.append(altura)

promedioAlturas = sum(alturas) / len(alturas)

masAltas = 0
masBajas = 0

for altura in alturas:
    if altura > promedioAlturas:
        masAltas += 1
    elif altura < promedioAlturas:
        masBajas += 1

print(f"Alturas ingresadas: {alturas}")
print(f"Promedio de alturas: {promedioAlturas:.2f} cm")
print(f"Cantidad de personas más altas que el promedio: {masAltas}")
print(f"Cantidad de personas más bajas que el promedio: {masBajas}")
