nombres = ["Carlos", "Ana", "Miguel", "Luis", "Sofía"]

contadorNombresLargos = 0

for nombre in nombres:
    if len(nombre) >= 5:
        contadorNombresLargos += 1

print(f"Cantidad de nombres con 5 o más caracteres: {contadorNombresLargos}")
