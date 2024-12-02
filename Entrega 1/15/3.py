sueldosManana = []
sueldosTarde = []

print("Ingrese los sueldos de los empleados del turno de la mañana:")
for i in range(4):
    sueldo = float(input(f"Sueldo del empleado {i + 1}: "))
    sueldosManana.append(sueldo)

print("Ingrese los sueldos de los empleados del turno de la tarde:")
for i in range(4):
    sueldo = float(input(f"Sueldo del empleado {i + 1}: "))
    sueldosTarde.append(sueldo)

print("Sueldos del turno de la mañana:", sueldosManana)
print("Sueldos del turno de la tarde:", sueldosTarde)


