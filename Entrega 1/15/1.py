sueldos = []

for i in range(5):
    sueldo = float(input(f"Ingrese el sueldo del operario {i + 1}: "))
    sueldos.append(sueldo)

print("Lista de sueldos:", sueldos)

promedioSueldos = sum(sueldos) / len(sueldos)

print(f"El promedio de los sueldos es: {promedioSueldos:.2f}")
