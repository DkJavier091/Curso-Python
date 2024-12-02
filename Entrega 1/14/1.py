lista = [120, 85, 200, 95, 150, 50, 300, 75]

contadorSuperiores_100 = 0

for valor in lista:
    if valor > 100:
        contadorSuperiores_100 += 1

print(f"Cantidad de valores superiores a 100: {contadorSuperiores_100}")
