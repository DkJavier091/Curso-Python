n = int(input("Ingrese el número de personas: "))

sumaAlturas = 0
contador = 0

while contador < n:
    altura = float(input("Ingrese la altura de la persona (en cm): "))
    sumaAlturas += altura
    contador += 1

promedioAlturas = sumaAlturas / n

print(f"La altura promedio de las personas es: {promedioAlturas:.2f} cm")
